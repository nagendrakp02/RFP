def assignment_fields():
    return [
        "Bid Number", "Title", "Due Date", "Bid Submission Type", "Term of Bid",
        "Pre Bid Meeting", "Installation", "Bid Bond Requirement", "Delivery Date",
        "Payment Terms", "Any Additional Documentation Required", "MFG for Registration",
        "Contract or Cooperative to use", "Model_no", "Part_no", "Product",
        "contact_info", "company_name", "Bid Summary", "Product Specification"
    ]

def empty_assignment_json():
    return {field: "" for field in assignment_fields()}
