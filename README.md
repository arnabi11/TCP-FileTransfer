# TCP-FileTransfer
<br>A python server client program, to send and recieve file over <strong>TCP/IP</strong> based sockets.
<br>It uses for python Tkinter and easygui modules for gui.
<br>Connect both pc to same wifi or hotspot
<br>Use <code>'ipconfig'</code>/<code>'ifconfig'</code> accordingly to find the IP of the server
<br>Run the <strong>Server</strong> on a pc from which you will send file 
<br>Run the <strong>Client</strong> on reciever pc, and enter the IP of server  

<h1>Usage</h1>
<h2>SERVER</h2>
<ul>
<li>Run the <code>fileServer.py</code> and answer the prompt for port number .</li>
<li>Server will be initialized, wait for client to connect</li>
<li>IF a client connects, it's IP will be displayed along with a notification on terminal</li>
<li>Prompt will appear if client demands a file</li>
<li>After <code>'OK'</code>, a file explorer dialog will appear ,<code> ->Select the file</code></li>
<li>After you click open file will be sent</li>
</ul>

<h2>CLIENT</h2>
<ul>
<li>Run <code>fileClient.py</code> and enter the IP of server, and the port no to bind with </li>
<li>Confirmation of Connection will be recieved on terminal</li>
<li>Ask for the file you want from the server</li>
<li>Answer the CONFIRM prompt, if you really want the file</li>
<li>After <code>'OK'</code>, a file explorer dialog appears , asking you to save the file, at the desired location</li>
<li>The file Tranfer starts, and the progess rate can be seen on terminal's console</li>
</ul>

#ENJOY!!!

