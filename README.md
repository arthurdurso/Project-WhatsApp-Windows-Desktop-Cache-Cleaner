# Clean WhatsApp's Cache

My first project on my own developing a project to clean the WhatsApp cache, aiming to improve the application's performance and increase execution speed. The project will involve creating a script or application to safely identify and remove unnecessary cache data without affecting important user conversations or data. Additionally, the project should include a scheduler to ensure WhatsApp's performance is significantly improved after the cache is cleared.

Using a python file to create the script with the libraries 'os' and 'shutil' verifying every file and subjectory on the directory path set with my user as default (i'm gonna change that everyone can use it on the next commits). 

Possible ways of schedule the task:
 - Task Scheduler (Windows);
 - Python (schedule);
 - Execute on Startup.

The best option should be 'Execute on Startup', because it will clear the cache every time the PC log in to have the best performance.

The Task Scheduler is a tradicional way to schedule on windows, but someone could use Linux and cannot be a way for them. Besides that if a time is defined, then could have sometines not running (E.g. PC turned off). If I have choosen the Python, the schedule would run every x hours, and the code should be running all the time, which is a bad thing.
