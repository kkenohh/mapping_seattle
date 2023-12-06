library(sf)
# Thinking of creating a summary page that shows the overall inspection
# Create data table from assets
geojson_file <- "Cleaned_Restaurant_Inspections.geojson"
sf_data <- st_read(geojson_file)
str(sf_data)

#Max Score Inspection, 98
max_score_insp <- max(sf_data$SCORE_INSPECTION, na.rm = TRUE)

#Max Violation Points, 25
sf_data$VIOLATIONPOINTS <- as.numeric(sf_data$VIOLATIONPOINTS)
max_violation_points <- max(sf_data$VIOLATIONPOINTS, na.rm = TRUE)

#Amount of Risks
risk <- table(sf_data$RISK)
count_rI <- risk_I["I"]         #608
count_rII <- risk_I["II"]       #887
count_rIII <- risk_I["III"]     #7081


