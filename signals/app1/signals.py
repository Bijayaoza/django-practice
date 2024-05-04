from django.contrib.auth.signals import user_logged_in,user_login_failed ,user_logged_out
from django.contrib.auth.models import User
from django.dispatch import receiver
#3 rd import chai decorator ko lagi ho
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete


@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("..........");
    print("Loged in signal");
    print("sender", sender);
    print("Request",request);
    print("user",user);
    print("user password",user.password);
    print(f'kwargs:{kwargs}');

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("..........");
    print("Loged out signal");
    print("sender", sender);
    print("Request",request);
    print("user",user);
    print(f'kwargs:{kwargs}');

@receiver(user_login_failed)
def log_fail(sender,credentials,request,**kwargs):
    print("..........");
    print("Loged out signal");
    print("sender", sender);
    print("Request",request);
    print("Credentials",credentials);
    print(f'kwargs:{kwargs}');

@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("..........");
    print("pre_saved signal");
    print("sender", sender);
    print("instances",instance);
    print(f'kwargs:{kwargs}');


@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("..........");
        print("new recrd");
        print("sender", sender);
        print("instances",instance);
        print("created",created);
        print(f'kwargs:{kwargs}');
    else:
        print("..........");
        print("updated recrd");
        print("sender", sender);
        print("instances",instance);
        print("created",created);
        print(f'kwargs:{kwargs}');

