# DevDesk Frequently Asked Questions

## What is DevDesk?

DevDesk is a software-as-a-service platform that provides APIs
and developer tools for building, deploying, and monitoring
applications.

## How do I create an API key?

API keys can be created from the DevDesk Developer Dashboard.

Navigate to:

Developer Dashboard → Settings → API Keys

API keys must be stored securely.

Never share API keys with support staff or include them in public
source-code repositories.

## Why am I getting a 401 error?

A 401 error usually indicates an authentication problem.

Check that:

1. Authentication credentials are present.
2. The credentials are valid.
3. The credentials have not expired.
4. The authentication format is correct.

Do not share authentication credentials with support.

## Why am I getting a 403 error?

A 403 error usually indicates that the authenticated user does
not have permission to perform the requested operation.

Check:

1. Whether the user has the required permissions.
2. Whether the API key has the required scope.
3. Whether the requested resource is accessible.
4. Whether an applicable usage or rate limit has been reached.

## Why am I getting a 404 error?

A 404 error may indicate that:

- The requested resource does not exist.
- The resource identifier is incorrect.
- The authenticated user does not have access to the resource.

Verify the resource identifier and permissions.

## Why am I getting a 429 error?

A 429 error indicates that the applicable rate limit has been
exceeded.

Reduce the request frequency and follow the documented retry
instructions.

## Why am I getting a 500 error?

A 500 error indicates an unexpected server-side problem.

Try the request again after a short delay.

If the problem continues, check the DevDesk status page and
contact support if necessary.

## Can I send my API key to the AI Support Engineer?

No.

Never send API keys, passwords, access tokens, or other
authentication secrets to the AI Support Engineer.

## When should I contact human support?

Contact human support when:

- Documented troubleshooting does not solve the problem.
- You suspect a security vulnerability.
- You experience possible data loss or corruption.
- The problem appears to affect multiple services.
- You need an action that the AI cannot perform.

## Can the AI Support Engineer access my account?

No.

The AI Support Engineer does not directly access customer
accounts or retrieve private customer information.

The AI can only provide assistance based on the information
provided by the customer and the available knowledge base.