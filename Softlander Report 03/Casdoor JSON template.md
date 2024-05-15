```json
{
  "organizations": [
    {
      "owner": "",
      "name": "",
      "displayName": "",
      "websiteUrl": "",
      "favicon": "",
      "passwordType": "plain",
      "passwordSalt": "",
      "passwordOptions": ["AtLeast6"],
      "countryCodes": ["US", "GB", "ES", "FR", "DE", "CN", "JP", "KR", "VN", "ID", "SG", "IN", "IT", "MY", "TR", "DZ", "IL", "PH", "NL", "PL", "FI", "SE", "UA", "KZ"],
      "defaultAvatar": "",
      "defaultApplication": "",
      "tags": [],
      "languages": ["en", "zh", "es", "fr", "de", "id", "ja", "ko", "ru", "vi", "it", "ms", "tr","ar", "he", "nl", "pl", "fi", "sv", "uk", "kk", "fa"],
      "masterPassword": "",
      "defaultPassword": "",
      "initScore": 2000,
      "enableSoftDeletion": false,
      "isProfilePublic": true,
      "accountItems": []
    }
  ],
  "applications": [
    {
      "owner": "",
      "name": "",
      "displayName": "",
      "logo": "",
      "homepageUrl": "",
      "organization": "",
      "cert": "",
      "enablePassword": true,
      "enableSignUp": true,
      "clientId": "",
      "clientSecret": "",
      "providers": [
        {
          "name": "",
          "canSignUp": true,
          "canSignIn": true,
          "canUnlink": false,
          "prompted": false,
          "alertType": "None"
        }
      ],
      "signinMethods": [
        {
          "name": "Password",
          "displayName": "Password",
          "rule": "All",
        },
        {
          "name": "Verification code",
          "displayName": "Verification code",
          "rule": "All",
        },
        {
          "name": "WebAuthn",
          "displayName": "WebAuthn",
          "rule": "None",
        },
      ],
      "signupItems": [
        {
          "name": "ID",
          "visible": false,
          "required": true,
          "prompted": false,
          "rule": "Random"
        },
        {
          "name": "Username",
            "visible": true,
            "required": true,
            "prompted": false,
            "rule": "None"
        },
        {
          "name": "Display name",
            "visible": true,
            "required": true,
            "prompted": false,
            "rule": "None"
        },
        {
          "name": "Password",
            "visible": true,
            "required": true,
            "prompted": false,
            "rule": "None"
        },
        {
          "name": "Confirm password",
            "visible": true,
            "required": true,
            "prompted": false,
            "rule": "None"
        },
        {
          "name": "Email",
            "visible": true,
            "required": true,
            "prompted": false,
            "rule": "None"
        },
        {
          "name": "Phone",
            "visible": true,
            "required": true,
            "prompted": false,
            "rule": "None"
        },
        {
          "name": "Agreement",
            "visible": true,
            "required": true,
            "prompted": false,
            "rule": "None"
        }
      ],
      "grantTypes": ["authorization_code", "password", "client_credentials", "token", "id_token", "refresh_token"],
      "redirectUris": [""],
      "expireInHours": 168,
      "failedSigninLimit": 5,
      "failedSigninFrozenTime": 15
    }
  ],
  "users": [
    {
      "owner": "",
      "name": "",
      "type": "normal-user",
      "password": "",
      "displayName": "",
      "avatar": "",
      "email": "",
      "phone": "",
      "countryCode": "",
      "address": [],
      "affiliation": "",
      "tag": "",
      "score": 2000,
      "ranking": 1,
      "isAdmin": true,
      "isForbidden": false,
      "isDeleted": false,
      "signupApplication": "",
      "createdIp": "",
      "groups": []
    }
  ],
  "providers": [
    {
      "owner": "",
      "name": "",
      "displayName": "",
      "category": "",
      "type": ""
    }
  ],
  "certs": [
    {
      "owner": "",
      "name": "",
      "displayName": "",
      "scope": "JWT",
      "type": "x509",
      "cryptoAlgorithm": "RS256",
      "bitSize": 4096,
      "expireInYears": 20,
      "certificate": "",
      "privateKey": ""
    }
  ],
  "ldaps": [
    {
      "id": "",
      "owner": "",
      "serverName": "",
      "host": "",
      "port": 389,
      "username": "",
      "password": "",
      "baseDn": "",
      "autoSync": 0,
      "lastSync": ""
    }
  ],
  "models": [
    {
      "owner": "",
      "name": "",
      "modelText": "",
      "displayName": ""
    }
  ],
  "permissions": [
    {
      "actions": [],
      "displayName": "",
      "effect": "",
      "isEnabled": true,
      "model": "",
      "name": "",
      "owner": "",
      "resourceType": "",
      "resources": [],
      "roles": [],
      "users": []
    }
  ],
  "payments": [
    {
      "currency": "",
      "detail": "",
      "displayName": "",
      "invoiceRemark": "",
      "invoiceTaxId": "",
      "invoiceTitle": "",
      "invoiceType": "",
      "invoiceUrl": "",
      "message": "",
      "name": "",
      "organization": "",
      "owner": "",
      "payUrl": "",
      "personEmail": "",
      "personIdCard": "",
      "personName": "",
      "personPhone": "",
      "price": 0,
      "productDisplayName": "",
      "productName": "",
      "provider": "",
      "returnUrl": "",
      "state": "",
      "tag": "",
      "type": "",
      "user": ""
    }
  ],
  "products": [
    {
      "currency": "",
      "detail": "",
      "displayName": "",
      "image": "",
      "name": "",
      "owner": "",
      "price": 0,
      "providers": [],
      "quantity": 0,
      "returnUrl": "",
      "sold": 0,
      "state": "",
      "tag": ""
    }
  ],
  "resources": [
    {
      "owner": "",
      "name": "",
      "user": "",
      "provider": "",
      "application": "",
      "tag": "",
      "parent": "",
      "fileName": "",
      "fileType": "",
      "fileFormat": "",
      "url": "",
      "description": ""
    }
  ],
  "roles": [
    {
      "displayName": "",
      "isEnabled": true,
      "name": "",
      "owner": "",
      "roles": [],
      "users": []
    }
  ],
  "syncers": [
    {
      "affiliationTable": "",
      "avatarBaseUrl": "",
      "database": "",
      "databaseType": "",
      "errorText": "",
      "host": "",
      "isEnabled": false,
      "name": "",
      "organization": "",
      "owner": "",
      "password": "",
      "port": 0,
      "syncInterval": 0,
      "table": "",
      "tableColumns": [
        {
          "casdoorName": "",
          "isHashed": true,
          "name": "",
          "type": "",
          "values": []
        }
      ],
      "tablePrimaryKey": "",
      "type": "",
      "user": ""
    }
  ],
  "tokens": [
    {
      "accessToken": "",
      "application": "",
      "code": "",
      "codeChallenge": "",
      "codeExpireIn": 0,
      "codeIsUsed": true,
      "createdTime": "",
      "expiresIn": 0,
      "name": "",
      "organization": "",
      "owner": "",
      "refreshToken": "",
      "scope": "",
      "tokenType": "",
      "user": ""
    }
  ],
  "webhooks": [
    {
      "contentType": "",
      "events": [],
      "headers": [
        {
          "name": "",
          "value": ""
        }
      ],
      "isEnabled": true,
      "isUserExtended": true,
      "method": "",
      "name": "",
      "organization": "",
      "owner": "",
      "url": ""
    }
  ],
  "groups": [
    {
        "owner": "",
        "name":"",
        "displayName": "",
        "manager": "",
        "contactEmail": "",
        "type": "",
        "parent_id": "",
        "isTopGroup": true,
        "title": "",
        "key": "",
        "children": "",
        "isEnabled": true
    }
  ],
  "adapters": [
    {
        "owner": "",
        "name": "",
        "table": "",
        "useSameDb": true,
        "type": "",
        "databaseType": "",
        "database": "",
        "host": "",
        "port": 0,
        "user": "",
        "password": "",
    }
  ],
  "enforcers": [
    {
        "owner": "",
        "name": "",
        "displayName": "",
        "description": "",
        "model": "",
        "adapter": "",
        "enforcer": ""
    }
  ],
  "plans": [
    {
        "owner": "",
        "name": "",
        "displayName": "",
        "description": "",
        "price": 0,
        "currency": "",
        "period": "",
        "product": "",
        "paymentProviders": [],
        "isEnabled": true,
        "role", ""
    }
  ],
  "pricings": [
    {
        "owner": "",
        "name": "",
        "displayName": "",
        "description": "",
        "plans": [],
        "isEnabled": true,
        "trialDuration": 0,
        "application": "",
    }
  ]
}
```

## Explanation of JSON Template

This file outlines the initial setup data for a Casdoor instance, including the structure and default settings for various entities such as organizations, applications, users, providers, certificates (certs), LDAP configurations, models, permissions, payments, products, resources, roles, syncers, tokens, webhooks, groups, adapters, enforcers, plans, and pricings. Here's a breakdown of key sections and their significance:

### Organizations
- **`organizations`**: Defines the initial setup for organizations within the Casdoor system, including ownership, display properties (name, display name, website URL, favicon), password policies (type, salt, options), country codes, default settings (avatar, application, password, score), deletion policies, and other organizational preferences.

### Applications
- **`applications`**: Specifies applications that will use Casdoor for authentication and authorization. It includes details about ownership, display properties (name, display name, logo, homepage URL), organizational association, security credentials (cert, clientId, clientSecret), authentication and sign-up settings, sign-in methods, sign-up item requirements, and other application-specific settings.

### Users
- **`users`**: Lists initial user accounts, including their type, authentication information (password, displayName, avatar), contact information (email, phone), location (countryCode), affiliations, and administrative status.

### Providers
- **`providers`**: Describes external authentication providers (e.g., OAuth providers) that Casdoor can integrate with, including their category and type.

### Certs
- **`certs`**: Contains information about certificates used for secure communication, specifying details like scope, type, algorithm, size, expiry, and key material.
- Here, we are using the inbuilt casdoor certificate

### LDAPs
- **`ldaps`**: Configures LDAP (Lightweight Directory Access Protocol) servers for directory services integration, detailing server information and synchronization settings.

### Models, Permissions, Payments, Products, Resources, Roles, Syncers, Tokens, Webhooks, Groups, Adapters, Enforcers, Plans, and Pricings
- These sections define additional aspects of the Casdoor ecosystem, including:
    - **`models`** and **`permissions`** for access control configurations,
    - **`payments`** and **`products`** for financial transactions and product management,
    - **`resources`**, **`roles`**, **`groups`** for resource access and organizational structuring,
    - **`syncers`** for external data synchronization,
    - **`tokens`** for API access control,
    - **`webhooks`** for event notifications,
    - **`adapters`**, **`enforcers`** for policy enforcement mechanisms,
    - **`plans`** and **`pricings`** for subscription management and pricing strategies.

This JSON template is highly configurable and allows for extensive customization to fit the specific needs of an organization or application relying on Casdoor for identity and access management. Each section's attributes must be filled out according to the system's requirements and the intended configuration for the Casdoor instance.
