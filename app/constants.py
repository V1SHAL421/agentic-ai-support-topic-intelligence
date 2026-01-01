primary_topics = [
    "Account Management",
    "Order Management",
    "Product Issues",
    "Returns & Exchanges",
    "Billing & Payment",
    "Warranty & Support",
    "Delivery & Shipping",
    "Inventory & Availability",
    "Pricing & Promotions",
    "Documentation & Training"
]

primary_to_secondary = {
    "Account Management": ["Login Issues", "Account Information Updates"],
    "Order Management": ["Order Status Updates", "Tracking Information"],
    "Product Issues": ["Defective Products", "Product Damage"],
    "Returns & Exchanges": ["Return Requests", "Exchange Requests"],
    "Billing & Payment": ["Payment Issues", "Invoice Queries"],
    "Warranty & Support": ["Warranty Claims", "Technical Support"],
    "Delivery & Shipping": ["Delivery Status", "Shipping Information"],
    "Inventory & Availability": ["Stock Issues"],
    "Pricing & Promotions": ["Pricing Discrepancies"],
    "Documentation & Training": ["Invoice Issues"]
}

secondary_to_tertiary = {
    "Login Issues": ["Mobile/Email Verification Problems", "Password Reset Requests", "Account Reactivation", "Exceeded Verification Attempts"],
    "Account Information Updates": ["Email Address Changes", "Mobile Number Verification", "Corporate Email Signup Issues"],
    "Order Status Updates": ["Delivery Status Inquiries", "Order Confirmation Checks", "Tracking Information Requests"],
    "Tracking Information": ["Delivery Status Inquiries", "Order Confirmation Checks", "Tracking Information Requests"],
    "Defective Products": ["Not Working Properly", "Damaged Upon Arrival", "Installation Problems"],
    "Product Damage": ["Wrong Items Received", "Incorrect Product Shipped", "Size/Model Mismatches"],
    "Return Requests": ["Return Eligibility", "Return Fees and Policies", "Prepaid Shipping Labels"],
    "Exchange Requests": ["Product Replacements", "Size Exchanges", "Defective Item Exchanges"],
    "Payment Issues": ["Cash on Delivery Problems", "Credit Card Payment Failures", "Billing Discrepancies"],
    "Invoice Queries": ["Missing Invoices", "Invoice Generation Problems", "Invoice Delivery to Email"],
    "Warranty Claims": ["Warranty Start Dates", "Warranty Terms and Conditions", "Warranty Claim Processes"],
    "Technical Support": ["Installation Assistance", "Product Troubleshooting", "Service Center Issues"],
    "Delivery Status": ["Delayed Deliveries", "Missing Packages", "Failed Delivery Attempts"],
    "Shipping Information": ["Faster Delivery Requests", "Shipping Availability by Location", "Delivery Time Estimates"],
    "Stock Issues": ["Out of Stock Products", "Availability Inquiries", "Waitlist Requests"],
    "Pricing Discrepancies": ["Different Prices for Same Products", "Hidden Charges", "Loyalty Points and Rewards"],
    "Invoice Issues": ["Missing Invoices", "Invoice Generation Problems", "Invoice Delivery to Email"]
}

"""
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
"""