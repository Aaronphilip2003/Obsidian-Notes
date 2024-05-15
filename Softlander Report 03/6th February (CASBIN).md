
```python
import base64
import binascii
import casbin
from fastapi import FastAPI
from starlette.authentication import AuthenticationBackend, AuthenticationError, SimpleUser, AuthCredentials
from starlette.middleware.authentication import AuthenticationMiddleware

# create a basic auth
class BasicAuth(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return None
        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise AuthenticationError("Invalid basic auth credentials")
        username, _, password = decoded.partition(":")
        return AuthCredentials(["authenticated"]), SimpleUser(username)

# create an enforcer
enforcer = casbin.Enforcer('./examples/rbac_model.conf', './examples/rbac_policy.csv')
# for the enforcer we need two files, the
# - rbac (role based access control) model config file
# - rbac policy file

# add the middlewares

app.add_middleware(CasbinMiddleware, enforcer=enforcer)
app.add_middleware(AuthenticationMiddleware, backend=BasicAuth())

@app.get('/')
async def index():
    return "If you see this, you have been authenticated."

@app.get('/dataset1/protected')
async def auth_test():
    return "You must be alice to see this."


```

`rbac_model.conf`
```
[request_definition]
r = sub, obj, act

[policy_definition]
p = sub, obj, act

[role_definition]
g = _, _

[policy_effect]
e = some(where (p.eft == allow))

[matchers]
m = (p.sub == "*" || g(r.sub, p.sub)) && (r.obj == p.obj || keyMatch(r.obj, p.obj)) && (p.act == "*" || r.act == p.act)
```

**rbac_model.conf:**
This file defines the model for the RBAC system. It consists of several sections:

Request Definition ([request_definition]):
Defines the components of a request: sub (subject), obj (object), and act (action).

Policy Definition ([policy_definition]):
Defines the structure of policies. Here, p denotes the components of a policy: sub (subject), obj (object), and act (action).

Role Definition ([role_definition]):
Defines the structure of roles. Here, g specifies the relationship between the roles.

Policy Effect ([policy_effect]):
Describes the policy effect. In this case, it's specified as e = some(where (p.eft == allow)), meaning if any policy allows the action, then it's permitted.

Matchers ([matchers]):
Defines how policies are evaluated. The matcher checks if the subject (sub) matches any role (g(r.sub, p.sub)), if the object (obj) matches any object in the policy, and if the action (act) matches any action in the policy.

 `rbac_policy.csv`
 ```
p, alice, /dataset1/*, GET
p, alice, /dataset1/resource1, POST
p, bob, /dataset2/resource1, *
p, bob, /dataset2/resource2, GET
p, bob, /dataset2/folder1/*, POST
p, dataset1_admin, /dataset1/*, *
p, *, /login, *
p, anonymous, /, GET
g, cathy, dataset1_admin
```

This file contains the actual policies for the RBAC system. Each line represents a policy rule with the following format:

```
p, subject, object, action
```
- p: Indicates that this line is a policy rule.
- subject: Represents the role or user to whom the policy applies.
- object: Denotes the resource or object being accessed.
- action: Specifies the action being performed on the resource.

Additionally, there is a line that starts with g, which is used for defining role relationships.

- g: Indicates a role relationship definition.
- cathy: The subject or role to which the role relationship applies.
- dataset1_admin: The role that cathy inherits permissions from.

*There's also a wildcard * used for generic matching, allowing any subject or object. This is often used for defining default rules or catch-all rules.*


This RBAC setup defines various permissions for different roles (alice, bob, dataset1_admin, etc.) to access different resources (/dataset1/, /dataset2/resource1, etc.) with different actions (e.g., GET, POST). Additionally, it defines a role relationship (cathy inherits permissions from dataset1_admin).