<h1 class="gap">AirBnB Clone Project - The console</h1>
<div class="gap formatted-content">
 <p><img src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="" style="" /></p>
</div>

<h2>Background Context</h2>

<h3>Welcome to the AirBnB clone project! (The Holberton B&amp;B)</h3>
<p>The goal of the project is to deploy on our server a simple copy of the <a href="https://www.airbnb.com.co/?_set_bev_on_new_domain=1603893429_NTkyMTA3NDhiYTAy" title="AirBnB website" target="_blank">AirBnB website</a>.</p>

<p>We won&rsquo;t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.</p>

<p>After 4 months, we will have a complete web application composed by:</p>

<ul>
<li>A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)</li>
<li>A website (the front-end) that shows the final product to everybody: static and dynamic</li>
<li>A database or files that store data (data = objects)</li>
<li>An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)</li>
</ul>

<h2>Steps</h2>

<p>We won&rsquo;t build this application all at once, but step by step.</p>

<p>Each step will link to a concept. This specific repository:</p>

<h3>The console</h3>

<ul>
<li>create our data model</li>
<li>manage (create, update, destroy, etc) objects via a console / command interpreter</li>
<li>store and persist objects to a file (JSON file)</li>
</ul>

<p>The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between &ldquo;My object&rdquo; and &ldquo;How they are stored and persisted&rdquo;. This means:
from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later.

<p>This abstraction will also allow us to change the type of storage easily without updating all of our codebase.</p>

<p>The console will be a tool to validate this storage engine</p>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7 or more)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>Python Unit Tests</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder <code>tests</code></li>
<li>You have to use the <a href="/rltoken/QX7d4D__xhOJIGIWZBp39g" title="unittest module" target="_blank">unittest module</a> </li>
<li>All your test files should be python files (extension: <code>.py</code>)</li>
<li>All your test files and folders should start by <code>test_</code></li>
<li>Your file organization in the tests folder should be the same as your project</li>
<li>e.g., For <code>models/base_model.py</code>, unit tests must be in: <code>tests/test_models/test_base_model.py</code></li>
<li>e.g., For <code>models/user.py</code>, unit tests must be in: <code>tests/test_models/test_user.py</code></li>
<li>All your tests should be executed by using this command: <code>python3 -m unittest discover tests</code></li>
<li>You can also test file by file by using this command: <code>python3 -m unittest tests/test_models/test_base_model.py</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
</ul>

<h2>Files and Directories</h2>
<ul>
<li><code>models</code> directory will contain all classes used for the entire project. A class, called &ldquo;model&rdquo; in a OOP project is the representation of an object/instance.</li>
<li><code>tests</code> directory will contain all unit tests.</li>
<li><code>console.py</code> file is the entry point of our command interpreter.</li>
<li><code>models/base_model.py</code> file is the base class of all our models. It contains common elements: 

<ul>
<li>attributes: <code>id</code>, <code>created_at</code> and <code>updated_at</code></li>
<li>methods: <code>save()</code> and <code>to_json()</code></li>
</ul></li>
<li><code>models/engine</code> directory will contain all storage classes (using the same prototype). For the moment you will have only one: <code>file_storage.py</code>.</li>
</ul>

<h2>More Info</h2>

<h3>Execution</h3>
<p>Interactive mode:</p>
<pre><code>$ ./console.py
(hbnb) help

EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
</code></pre>

<p>Non-interactive mode:</p>
<pre><code>$ echo &quot;help&quot; | ./console.py
(hbnb)

EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

EOF  help  quit
(hbnb)
$
</code></pre>


<h2>Installation</h2>
<ul>
<li> git clone </li>
<li> cd AirBnB_clone </li>
<li> ./console.py </li>
</ul>


<h2 class="gap"> Authors </h2>
<p> Steffany Naranjo Vargas - <strong>GitHub</strong> <a href="https://github.com/steffanynaranjov">steffanynaranjov</a></p>
<p> Diana Sofía García Caicedo - <strong>GitHub</strong> <a href="https://github.com/Sofiag8">Sofiag8</a></p>