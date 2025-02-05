-- COCOON BLOCK START: PLEASE DO NOT MODIFY THIS BLOCK FOR SELF-MAINTENANCE
WITH 
"usage_platform_version_source_type_projected" AS (
    -- Projection: Selecting 10 out of 11 columns
    -- Columns projected out: ['_fivetran_synced']
    SELECT 
        "app_id",
        "date_",
        "platform_version",
        "source_type",
        "meets_threshold",
        "installations",
        "sessions",
        "active_devices",
        "active_devices_last_30_days",
        "deletions"
    FROM "usage_platform_version_source_type"
),

"usage_platform_version_source_type_projected_renamed" AS (
    -- Rename: Renaming columns
    -- date_ -> record_date
    -- platform_version -> os_version
    -- source_type -> acquisition_source
    -- installations -> daily_installations
    -- sessions -> daily_sessions
    -- active_devices -> daily_active_devices
    -- active_devices_last_30_days -> monthly_active_devices
    -- deletions -> daily_deletions
    SELECT 
        app_id,
        date_ AS record_date,
        platform_version AS os_version,
        source_type AS acquisition_source,
        meets_threshold,
        installations AS daily_installations,
        sessions AS daily_sessions,
        active_devices AS daily_active_devices,
        active_devices_last_30_days AS monthly_active_devices,
        deletions AS daily_deletions
    FROM usage_platform_version_source_type_projected
),

"usage_platform_version_source_type_projected_renamed_casted" AS (
    -- Column Type Casting: 
    -- app_id: from INT to VARCHAR
    -- record_date: from VARCHAR to TIMESTAMP
    SELECT
        "os_version",
        "acquisition_source",
        "meets_threshold",
        "daily_installations",
        "daily_sessions",
        "daily_active_devices",
        "monthly_active_devices",
        "daily_deletions",
        CAST("app_id" AS VARCHAR) AS "app_id",
        CAST("record_date" AS TIMESTAMP) AS "record_date"
    FROM "usage_platform_version_source_type_projected_renamed"
)

-- COCOON BLOCK END
SELECT * FROM "usage_platform_version_source_type_projected_renamed_casted"