# Jeremiasz Mozgwa - thesis

## To run backend you need to:
    - Go to Backend catalog and activate python environment with . venv/bin/activate
    - Set flask environment variables with:
    export FLASK_APP=flaskr
    export FLASK_ENV=development
    export FLASK_RUN_PORT=7000
    - run serwer with: flask run
## when backend server is running to run frontend: "dotnet run" and go to localhost:5001
## login: test, pw: test



Now endpoint is available for posting under the URL : http://127.0.0.1:7000/convert/simple

As requested - in order to avoid any JavaScript this app uses ASP.NET Core Blazor WebAssembly.

I spent a couple of days fiddling around and trying to make a simple http mockup to allow user login and logout.
I ended up making a mockup of backend (./Helpers/FakeBackendHandler.cs) and a couple of services to handle async requests (./Serivces).
Right now its extremely easy to relinqish the login process to external api - all you have to do is switch flag to false in wwwroot/apsettings.json and provide the api url.

All the work with fakebackend was based on the ("fake" - oh god no) premise that i would not have to use any backend to run the app. (at least in its alfa stage for thesis) I thought that i could run python scripts from inside the c# logic in razor files no problem and show its results to the user. I couldn't and i won't. This is why:

- c# can create and run new side processes (look Preview.razor run_cmd method) but ONLY in server environment (not client one). Since this app is webassembled we might get away with running python code on init (before build) but not asynchronously and while the app is working.

I tried the c# way of handling python (the IronPython library) with moderate success, but the library is dead and it does not support python 3 (which im almost certain will be used in final model) so i discarded it.

### Hitherto conclusions:

#### Advantages:  
    - Syntax is very similar to Svelte and React - (using HTML alongside logic (c#) - in .razor files)

#### Disadvantages: 
    - ASP.NET is huge and feels like it does not know which direction it wants to develop ( documentation is enormous, consisting of ASP .NET Core, MVC , Razor, Blazor etc.). This makes things hard to google and easy to mix up.
    Feels like early Angular beta and 2.0 fiasco.
    - The online community is extremely small.
    - C# leaves a lot of boiler around - the code is less consise.
    - File importing and dependency injection is is ambigous to say the least

