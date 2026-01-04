repair_prompt = """
You produced an INVALID classification.

Fix it so that:
- Output is a SINGLE valid JSON object
- Output contains ONLY these keys:
  primary_topic, secondary_topic, tertiary_topic, confidence
- Use ONLY labels from the taxonomy
- Do NOT add explanations or extra text
- INCLUDE ALL FOUR KEYS EVEN IF NULL

Customer Support Topics
├── Account Management
│   ├── Login Issues
│   │   ├── Mobile/Email Verification Problems
│   │   ├── Password Reset Requests
│   │   ├── Account Reactivation
│   │   └── Exceeded Verification Attempts
│   └── Account Information Updates
│       ├── Email Address Changes
│       ├── Mobile Number Verification
│       └── Corporate Email Signup Issues
│
├── Order Management
│   ├── Order Status & Tracking
│   │   ├── Delivery Status Inquiries
│   │   ├── Order Confirmation Checks
│   │   └── Tracking Information Requests
│   └── Order Modifications
│       ├── Address Changes for Pickup/Delivery
│       ├── Cancellation Requests
│       └── Expedited Shipping Requests
│
├── Product Issues
│   ├── Defective Products
│   │   ├── Not Working Properly
│   │   ├── Damaged Upon Arrival
│   │   └── Installation Problems
│   └── Wrong Items Received
│       ├── Incorrect Product Shipped
│       └── Size/Model Mismatches
│
├── Returns & Exchanges
│   ├── Return Processes
│   │   ├── Return Eligibility
│   │   ├── Return Fees and Policies
│   │   └── Prepaid Shipping Labels
│   └── Exchange Requests
│       ├── Product Replacements
│       ├── Size Exchanges
│       └── Defective Item Exchanges
│
├── Billing & Payment
│   ├── Payment Issues
│   │   ├── Cash on Delivery Problems
│   │   ├── Credit Card Payment Failures
│   │   └── Billing Discrepancies
│   └── Refunds
│       ├── Refund Status Checks
│       ├── Refund Processing Times
│       └── Courier Charge Reimbursements
│
├── Warranty & Support
│   ├── Warranty Information
│   │   ├── Warranty Start Dates
│   │   ├── Warranty Terms and Conditions
│   │   └── Warranty Claim Processes
│   └── Technical Support
│       ├── Installation Assistance
│       ├── Product Troubleshooting
│       └── Service Center Issues
│
├── Delivery & Shipping
│   ├── Delivery Problems
│   │   ├── Delayed Deliveries
│   │   ├── Missing Packages
│   │   └── Failed Delivery Attempts
│   └── Shipping Options
│       ├── Faster Delivery Requests
│       ├── Shipping Availability by Location
│       └── Delivery Time Estimates
│
├── Inventory & Availability
│   └── Stock Issues
│       ├── Out of Stock Products
│       ├── Availability Inquiries
│       └── Waitlist Requests
│
├── Pricing & Promotions
│   └── Pricing Discrepancies
│       ├── Different Prices for Same Products
│       ├── Hidden Charges
│       └── Loyalty Points and Rewards
│
└── Documentation
    └── Invoice Issues
        ├── Missing Invoices
        ├── Invoice Generation Problems
        └── Invoice Delivery to Email

Original output:
"""