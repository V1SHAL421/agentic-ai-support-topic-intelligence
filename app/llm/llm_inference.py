from vllm import LLM, SamplingParams

def infer(model, input_data):
    if isinstance(model, str):
        model = LLM(model=model)
    else:
        llm = model

    sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
    outputs = llm.generate(input_data, sampling_params)

    