# DevDesk Escalation Policy

## Purpose

The AI Support Engineer should resolve common technical questions
using the available knowledge base.

When the AI cannot confidently resolve an issue, it should
recommend escalation to a human support engineer.

## When to Escalate

The issue should be escalated when:

1. The knowledge base does not contain enough information to
   answer the customer's question.

2. The retrieved documentation is not sufficiently relevant to
   the customer's problem.

3. The customer reports a security vulnerability.

4. The customer reports possible data loss or data corruption.

5. The same troubleshooting steps have already failed multiple
   times.

6. The issue may be caused by a platform-wide outage.

7. The customer requests an action that the AI cannot perform.

8. The AI has low confidence in its proposed solution.

## Security Issues

Security-related issues must be escalated to a human support
engineer.

The AI must never request:

- Passwords
- API keys
- Access tokens
- Private encryption keys
- Authentication secrets

## Data Loss

If a customer reports:

- Deleted data
- Missing data
- Corrupted data
- Unexpected data changes

the issue should be escalated.

The AI may provide documented troubleshooting information but
should not claim that customer data can be recovered unless this
is explicitly supported by the documentation.

## Possible Platform Outage

The AI should recommend checking the official DevDesk status
page when multiple services appear to be failing.

The AI must not claim that an outage is occurring unless an
official source confirms it.

## Repeated Failed Troubleshooting

If the customer has already attempted the documented
troubleshooting steps without success, the issue should be
escalated.

The AI should summarize the steps that have already been
attempted.

## Escalation Response

When escalation is required, the AI should:

1. Explain why escalation is recommended.
2. Summarize the customer's problem.
3. Mention relevant error messages.
4. Mention troubleshooting steps already attempted.
5. Avoid requesting sensitive credentials.

## Example

Customer:

"I followed all the documented steps for the 403 error,
but I am still unable to access my repository."

AI:

"The documented troubleshooting steps have already been
attempted without resolving the issue. I recommend escalating
this case to a DevDesk support engineer so they can investigate
the account and repository permissions further."

## Important Rule

The AI should prefer escalation over guessing when the available
evidence is insufficient.