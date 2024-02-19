from dataclasses import dataclass


# class for customer information
@dataclass
class Customer:
    cust_id: int
    first_name: str
    last_name: str
    company_name: str
    address: str
    city: str
    state: str
    zip: str

# full customer name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# full customer address
    @property
    def full_address(self):
        if self.company_name == "":
            location = f"{self.address}\n{self.city}, {self.state} {self.zip}"
        else:
            location = f"{self.company_name}\n{self.address}\n{self.city}, {self.state} {self.zip}"
        return location
