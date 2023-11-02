layer = iface.activeLayer()

layer.startEditing()

field_names = [field.name() for field in layer.fields()]

# Loop calculate population density
for year in range(1995, 2021):
  population_field = f"transformed_seoul_pop_data_{year}"
  density_field = f"pop_den_{year}"
  
  # Check if the density field already exists
  if density_field not in field_names:
    layer.addAttribute(QgsField(density_field, QVariant.Double, "double", 10, 2))

  # Calculate population density
  for feature in layer.getFeatures():
    population = feature[population_field]
    area = feature.geometry().area() * 10000
    if area > 0:
      density = population / area
      feature[density_field] = density
      layer.updateFeature(feature)
            

layer.commitChanges()
layer.triggerRepaint()

