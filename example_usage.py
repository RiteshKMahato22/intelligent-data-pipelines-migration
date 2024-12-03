# example_usage.py
from core.pipeline_model import Pipeline, PipelineStep
from adapters.databricks_adapter import DatabricksAdapter
from adapters.adf_adapter import ADFAdapter
from core.translation import PipelineTranslator

# Create a Databricks pipeline
pipeline = Pipeline()

# Step 1: Ingestion (e.g., reading from a CSV file in Databricks)
pipeline.add_step(PipelineStep('ingestion', {'source': 'databricks', 'config': {'format': 'csv', 'path': '/path/to/data'}}))

# Step 2: Transformation (e.g., filtering rows in Databricks)
pipeline.add_step(PipelineStep('transformation', {'transformation_type': 'filter', 'parameters': {'column': 'age', 'value': 30}}))

# Step 3: Output (writing to Parquet in Databricks)
pipeline.add_step(PipelineStep('output', {'destination': 'adf', 'config': {'output_path': '/path/to/output'}}))

# Create the source (Databricks) and target (ADF) adapters
databricks_adapter = DatabricksAdapter()
adf_adapter = ADFAdapter()

# Translate the pipeline from Databricks to ADF
translator = PipelineTranslator(databricks_adapter, adf_adapter)
translator.translate(pipeline)

# Execute the translated pipeline (on Azure Data Factory)
translator.execute(pipeline)
