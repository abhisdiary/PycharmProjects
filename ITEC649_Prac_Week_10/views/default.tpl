<html>
    <head><title>{{title}}</title></head>
    <body>
         <h1>{{!title}}</h1>

         <p><a href="/">Home</a></p>

         % if messages:
         <ul>
             % for m in messages:
              <li>{{!m}}</li>
             % end
         </ul>
         % end

          <form method='POST' action='/messages'>
                <input name='message' size="50" autofocus><input type='submit'>
          </form>

        <p>Welcome to CHAT, you can enter messages to chat with other users
        use #tags in your messages which will be turned into links to go
        to a page listing all messages with that tag.  Eg. <a href="/tag/CHAT">#CHAT</a>.</p>

    </body>
</html>
