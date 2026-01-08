"""Contains all stream schemas."""

from singer_sdk.typing import (
    DateTimeType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

sessions_schema = PropertiesList(
    Property("id", StringType, description="unique identifier for the session"),
    Property(
        "channel",
        ObjectType(
            Property("type", StringType, description="type of channel (e.g., web, mobile)"),
        ),
    ),
    Property("language", StringType, description="language of the conversation"),
    Property(
        "handoff",
        ObjectType(
            Property("sentiment", StringType, description="user sentiment at time of handoff"),
            Property("summary", StringType, description="summary of conversation at time of handoff"),
        ),
    ),
    Property(
        "ticketing_system",
        ObjectType(
            Property("external_id", StringType, description="external (i.e. intercom) id of the conversation"),
            Property("name", StringType, description="name of the application"),
            Property(
                "id_type",
                StringType,
                description="id type of the ticketing system",
                allowed_values=["conversation_id", "ticket_id", "case_id", "conversation_sid"],
            ),
        ),
    ),
    Property("created_at", DateTimeType, description="session created timestamp (ISO 8601)"),
    Property("updated_at", DateTimeType, description="session updated timestamp (ISO 8601)"),
).to_dict()
