from typing import TypedDict, Optional
from pydantic import BaseModel, Field

class RFPData(BaseModel):
    Bid_Number: str = Field(default="")
    Title: str = Field(default="")
    Due_Date: str = Field(default="")
    Bid_Submission_Type: str = Field(default="")
    Term_of_Bid: str = Field(default="")
    Pre_Bid_Meeting: str = Field(default="")
    Installation: str = Field(default="")
    Bid_Bond_Requirement: str = Field(default="")
    Delivery_Date: str = Field(default="")
    Payment_Terms: str = Field(default="")
    Any_Additional_Documentation_Required: str = Field(default="")
    MFG_for_Registration: str = Field(default="")
    Contract_or_Cooperative_to_use: str = Field(default="")
    Model_no: str = Field(default="")
    Part_no: str = Field(default="")
    Product: str = Field(default="")
    contact_info: str = Field(default="")
    company_name: str = Field(default="")
    Bid_Summary: str = Field(default="")
    Product_Specification: str = Field(default="")

class RFPState(TypedDict, total=False):
    file_path: str
    extracted_text: str
    rfp_data: RFPData
