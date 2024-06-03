## Bulk Payments Entry

ERPNext Bulk Payments Entry allows easy capture of non-item expenses without using the Journal Entry,

## Doctype Setup
#### Bulk Payments Entry Doctype
```
Users
- Accounts Users - can draft
- Payments Approver - can submit

Doctype Fields - BPY-.YEAR.-#####

- Company
- Date
- Payment Mode (link)

Accounting Dimensions:
- Default Cost Center (Link)
- Default Project (Link)

Section and Table: Bulk Payments Details
- Bulk Payments Account - (Required: Link - Filtered by Payments)
- Party Type
- Party
- Amount (Required: Currency)
- Cost Center

Section: Additional Information
- Remarks (Short text)
- Approved By (Read-only)

- column break
- Reference
- Reference Date
```

#### Accounts Settings (Customisation)
- Default Mode of Payment
- Alert Approvers (check)
- Automatically create Journal Entries


## Bulk Payments Workflow
1. Draft
2. Pending
2. Approved
3. Rejected
4. Cancelled

## Installation

```
bench get-app https://github.com/adesinasam/bulk_payments.git
bench --site site-name install-app bulk_payments
```


#### License

MIT
