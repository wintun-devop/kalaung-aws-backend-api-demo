import aws_cdk as core
import aws_cdk.assertions as assertions

from backend_api_stack.backend_api_stack_stack import BackendApiStackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in backend_api_stack/backend_api_stack_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BackendApiStackStack(app, "backend-api-stack")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
