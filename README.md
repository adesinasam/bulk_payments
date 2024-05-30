## Expense Entry (Renamed)

ERPNext Expense Entry allows easy capture of non-item expenses without using the Journal Entry,

## Doctype Setup
#### Expense Entry Doctype
```
Users
- Accounts Users - can draft
- Expense Approver - can submit

Doctype Fields - EXP-.YEAR.-#####

- Company
- Request Date (Auto: Read-only Datetime)
- Required Date (Required: Date)
- Payment To

Accounting Dimensions:
- Default Cost Center (Link)
- Default Project (Link)

Section and Table: Expense Details
- Expense Account - (Required: Link - Filtered by Expenses)
- Description - (Data)
- Amount (Required: Currency)
- Cost Center
- Project

Section: Additional Information
- Remarks (Short text)
- Approved By (Read-only)

- column break
- Payment Mode (link)
- Reference
- Reference Date
```

#### Accounts Settings (Customisation)
- Default Mode of Payment
- Alert Approvers (check)
- Automatically create Journal Entries


## Expense Workflow
1. Draft
2. Pending
2. Approved
3. Rejected
4. Cancelled

## Installation

```
bench get-app https://github.com/adesinasam/expense_journal.git
bench --site site-name install-app expense_journal
```


#### License

MIT
