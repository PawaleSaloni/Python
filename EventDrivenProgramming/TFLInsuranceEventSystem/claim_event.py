from claim_handlers import (
    validate_claim,
    notify_customer,
    notify_claims_officer,
    update_audit_log
)

def register_claim_handlers(dispatcher):

    dispatcher.subscribe("ClaimSubmitted", validate_claim)

    dispatcher.subscribe("ClaimSubmitted", notify_customer)

    dispatcher.subscribe("ClaimSubmitted", notify_claims_officer)

    dispatcher.subscribe("ClaimSubmitted", update_audit_log)