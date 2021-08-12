# basic-calc
Basic calculator web app
<!DOCTYPE html>
<html>
<body>

<h1>Basic Calculator</h1>
<h2>Web UI for a basic calculator</h2>

<form action="/success" method="post" enctype="multipart/form-data">
  <label for="input1">Enter First number(a)</label><br>
  <input type="number" id="input1" name="value_a" value="5"><br><br>
  <label for="input2">Enter Second number(b)</label><br>
  <input type="number" id="input2" name="value_b" value="5"><br><br>
  <label for="oper">Select the arithmetic operation:</label><br>
  <select id="oper" name="oper">
     <option value="+">a+b</option>
     <option value="-">a-b</option>
     <option value="*">a*b</option>
     <option value="/">a/b</option>
  </select><br><br>
  <p>Load Data:</p>
  <input type="file" name="file" required />
  <input type = "submit" value="Train">
</form>


</body>
</html>
