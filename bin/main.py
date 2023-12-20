import sys
import autogen
config_list = [
    {
       'model': 'gpt-3.5-turbo-16k',
        'api_key': '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',
    }
]

llm_config={
    "request_timeout":600,
    "seed":42,
    "config_list":config_list,
    "temperature":0
    
}


assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "request_timeout":600,
        "seed": 41,
        "config_list": config_list,
    }
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
)
autogen.ChatCompletion.start_logging()

supplier = sys.argv[1];

user_proxy.initiate_chat(assistant, message=supplier)