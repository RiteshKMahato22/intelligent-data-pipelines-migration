# pipeline_model.py
class PipelineStep:
    def __init__(self, step_type, config=None):
        self.step_type = step_type  # 'ingestion', 'transformation', 'output'
        self.config = config or {}

class Pipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, step: PipelineStep):
        self.steps.append(step)

    def get_steps(self):
        return self.steps

# Example of usage:
# pipeline = Pipeline()
# pipeline.add_step(PipelineStep('ingestion', {'source': 'databricks', 'config': {}}))
# pipeline.add_step(PipelineStep('transformation', {'transformation_type': 'filter', 'parameters': {'column': 'age', 'value': 30}}))
# pipeline.add_step(PipelineStep('output', {'destination': 'adf', 'config': {}}))
