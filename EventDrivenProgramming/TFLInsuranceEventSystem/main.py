from event_dispatcher import EventDispatcher
from claim_event import register_claim_handlers
from claim_data import claim


# Create EventDispatcher
dispatcher = EventDispatcher()


# Register handlers
register_claim_handlers(dispatcher)


# Publish event
dispatcher.publish("ClaimSubmitted",claim)