from django.shortcuts import HttpResponse
# # function middleware
# def my_middleware(get_response):
#     print('one time execution')
#     def my_function(request):
#         print('this is before view')
#         response = get_response(request)
#         print('this  is after view')
#         return response
#     return my_function

#class middleware

class Brothermiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('one time initialization of brother')

    def __call__(self,request):
        print('this is  before view of brother')
        response= self.get_response(request)
        print('this is after view of brother')
        return response
    
class Fathermiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('one time initialization of father')

    def __call__(self,request):
        print('this is  before view of father')
        # response= self.get_response(request)
        response=HttpResponse('middleware break')#here response is send from middleware no need to go to view
        print('this is after view of  father')
        return response

class Mothermiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print('one time initialization of mother')

    def __call__(self,request):
        print('this is  before view of mother')
        response= self.get_response(request)
        print('this is after view of mother')
        return response

#middleware hooks
class TemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_template_response(self,request,response):
        print('process template response from middleware')
        response.context_data['name']='bj'
        return response
    