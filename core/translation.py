# translation.py
class PipelineTranslator:
    def __init__(self, source_adapter, target_adapter):
        self.source_adapter = source_adapter
        self.target_adapter = target_adapter

    def translate(self, pipeline):
        print("Translating pipeline from Databricks to Azure Data Factory...")
        # Translate Databricks pipeline to the unified model
        self.source_adapter.translate_pipeline(pipeline)
        
        # Then translate the unified model into Azure Data Factory format
        self.target_adapter.translate_pipeline(pipeline)

    def execute(self, pipeline):
        self.target_adapter.execute_pipeline(pipeline)  # Execute the translated ADF pipeline
