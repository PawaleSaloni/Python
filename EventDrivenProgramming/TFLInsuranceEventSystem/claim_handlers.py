def validate_claim(data):

    print("Validating claim:", data["claim_id"])

    if data["amount"] <= 0:
        print("Invalid claim amount")
        return

    print("Claim validation completed")


def notify_customer(data):

    print("Sending claim acknowledgement to:",
          data["customer_email"])


def notify_claims_officer(data):

    print("Notifying claims officer about:",
          data["claim_id"])


def update_audit_log(data):

    print("Recording claim submission in audit log")