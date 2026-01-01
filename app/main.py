from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

"""
Primary:
Account Management, Order Management, Product Issues, Returns & Exchanges, Billing & Payment,
Warranty & Support, Delivery & Shipping, Inventory & Availability, Pricing & Promotions, Documentation

Secondary:
Login Issues, Account Information Updates, Order Status & Tracking, Order Modifications, Defective Products,
Wrong Items Received, Return Processes, Exchange Requests, Payment Issues, Refunds, Warranty Information,
Technical Support, Delivery Problems, Shipping Options, Stock Issues, Pricing Discrepancies, Invoice Issues

Tertiary:
Mobile/Email Verification Problems, Password Reset Requests, Account Reactivation, Exceeded Verification Attempts,
Email Address Changes, Mobile Number Verification, Corporate Email Signup Issues, Delivery Status Inquiries,
Order Confirmation Checks, Tracking Information Requests, Address Changes for Pickup/Delivery, Cancellation Requests,
Expedited Shipping Requests, Not Working Properly, Damaged Upon Arrival, Installation Problems, Incorrect Product Shipped,
Size/Model Mismatches, Return Eligibility, Return Fees and Policies, Prepaid Shipping Labels, Product Replacements,
Size Exchanges, Defective Item Exchanges, Cash on Delivery Problems, Credit Card Payment Failures, Billing Discrepancies,
Refund Status Checks, Refund Processing Times, Courier Charge Reimbursements, Warranty Start Dates,
Warranty Terms and Conditions, Warranty Claim Processes, Installation Assistance, Product Troubleshooting,
Service Center Issues, Delayed Deliveries, Missing Packages, Failed Delivery Attempts, Faster Delivery Requests,
Shipping Availability by Location, Delivery Time Estimates, Out of Stock Products, Availability Inquiries, Waitlist Requests,
Different Prices for Same Products, Hidden Charges, Loyalty Points and Rewards, Missing Invoices, Invoice Generation Problems,
Invoice Delivery to Email



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