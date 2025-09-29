"""Contains all stream schemas."""

from singer_sdk.typing import (
    ArrayType,
    DateTimeType,
    IntegerType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

insights_schema = PropertiesList(
    Property("id", StringType, description="The unique identifier for the customer insight"),
    Property("type", StringType, description="The type/category code of the insight"),
    Property("content", StringType, description="The main content or description of the insight"),
    Property("sentiment", StringType, description="The sentiment classification (e.g., NEGATIVE, POSITIVE)"),
    Property("category", StringType, description="The category of the insight"),
    Property("created_at", DateTimeType, description="Timestamp when the insight was created (ISO 8601)"),
    Property("updated_at", DateTimeType, description="Timestamp when the insight was last updated (ISO 8601)"),
    Property("occurrence_count", IntegerType, description="Number of sessions relating to the insight"),
    Property("is_resolved", IntegerType, description="Resolution status (0 = unresolved, 1 = resolved)"),
    Property("resolved_at", DateTimeType, description="Timestamp when the insight was resolved (ISO 8601, nullable)"),
    Property("resolved_by", StringType, description="Identifier of the user who resolved the insight (nullable)"),
    Property("group_id", StringType, description="Group identifier for related insights (nullable)"),
    Property("user_story", StringType, description="User story or narrative associated with the insight"),
    Property(
        "last_seen_at", DateTimeType, description="Timestamp when the insight was last seen in a session (ISO 8601)"
    ),
    # might want to add the embedding later if we there's a use case, leaving out for now
    # Property(
    #     "embedding",
    #     ArrayType(StringType),
    #     description="Vector embedding representing the insight content",
    # ),
    Property("is_snoozed", IntegerType, description="Snooze status (0 = not snoozed, 1 = snoozed)"),
    Property("snoozed_at", DateTimeType, description="Timestamp when the insight was snoozed (ISO 8601)"),
    Property("snoozed_by", StringType, description="Identifier of the user who snoozed the insight"),
    Property("deep_research", StringType, description="Detailed research or analysis related to the insight"),
    Property(
        "generating_deep_research", IntegerType, description="Flag indicating if deep research is being generated"
    ),
    Property("is_removed", IntegerType, description="Removal status (0 = active, 1 = removed)"),
    Property("sessions", ArrayType(StringType), description="List of session IDs associated with the insight"),
).to_dict()

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
        ),
    ),
    Property("created_at", DateTimeType, description="session created timestamp (ISO 8601)"),
    Property("updated_at", DateTimeType, description="session updated timestamp (ISO 8601)"),
).to_dict()
