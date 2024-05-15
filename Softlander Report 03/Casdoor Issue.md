
---

**Title**: Changes from `init_data.json` Not Reflected in UI

### Description

After initializing Casdoor with a custom `init_data.json` file, the specified configuration does not appear to be reflected in the Casdoor UI. The JSON file includes configurations for organizations, applications, and users. While the Docker container initializes without errors and the logs indicate the configuration is loaded, the expected entities are not visible in the UI.

Docs for the `init_data.json` can be found here:
https://casdoor.org/docs/deployment/data-initialization

### Steps to Reproduce

1. Prepare a `init_data.json` file with the following content:

```json
{
  "organizations": [
    {
      "owner": "testOrgOwner",
      "name": "testOrg",
      "displayName": "Test Organization",
      "websiteUrl": "http://example.com",
      "favicon": "http://example.com/favicon.ico",
      "passwordType": "plain",
      "passwordSalt": "",
      "passwordOptions": ["AtLeast6"],
      "countryCodes": ["US"],
      "defaultAvatar": "http://example.com/default-avatar.png",
      "defaultApplication": "testApp",
      "tags": ["test", "sample"],
      "languages": ["en"],
      "masterPassword": "",
      "defaultPassword": "password123",
      "initScore": 1000,
      "enableSoftDeletion": true,
      "isProfilePublic": true,
      "accountItems": []
    }
  ],
  "applications": [
    {
      "owner": "testAppOwner",
      "name": "testApp",
      "displayName": "Test Application",
      "logo": "http://example.com/logo.png",
      "homepageUrl": "http://example.com",
      "organization": "testOrg",
      "cert": "",
      "enablePassword": true,
      "enableSignUp": true,
      "clientId": "testClientId",
      "clientSecret": "testSecret",
      "providers": [],
      "signinMethods": [],
      "signupItems": [],
      "grantTypes": [],
      "redirectUris": [],
      "expireInHours": 24,
      "failedSigninLimit": 5,
      "failedSigninFrozenTime": 10
    }
  ],
  "users": [
    {
      "owner": "testUserOwner",
      "name": "testUser",
      "type": "normal-user",
      "password": "userPass",
      "displayName": "Test User",
      "avatar": "http://example.com/user-avatar.png",
      "email": "user@example.com",
      "phone": "+123456789",
      "countryCode": "US",
      "address": [],
      "affiliation": "Test Organization",
      "tag": "test",
      "score": 100,
      "ranking": 1,
      "isAdmin": false,
      "isForbidden": false,
      "isDeleted": false,
      "signupApplication": "testApp",
      "createdIp": "127.0.0.1",
      "groups": []
    }
  ]
}
```

2. Run the Docker container with the volume mount option to include the `init_data.json`:

```bash
docker run -d -p 8000:8000 -v /path/to/init_data.json:/init_data.json casdoor/casdoor:latest
```

*In our case, the` init_data.json` file gets updated on the docker image when there is a change*

3. Access the Casdoor UI at `http://localhost:8000`.

### Expected Behavior

The UI should display the organization, application, and user as defined in the `init_data.json` file.

### Actual Behavior

The configurations from `init_data.json` are not visible in the UI. There are no errors in the Docker logs to indicate a problem with loading the configuration.

### Environment

- Casdoor Version: [casbin/casdoor:latest]
- Deployment Method: Docker
- Browser: [Chrome]

---
