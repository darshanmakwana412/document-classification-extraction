from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["customer photograph", "Utility Bill", "Cheque Leaf", "Salary Slip", "Driving License", "PAN card", "Aadhaar front", "Aadhaar back", "Bank Statement", "ITR Form 16", "Voter ID", "Passport"]

for keyword in keywords:
    response().download(keyword, 100)