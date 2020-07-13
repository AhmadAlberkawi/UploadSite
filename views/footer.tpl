 </div>
</div>			
	
	%setdefault('error_messages', [])
	% for m in error_messages:
	<div class="alert alert‐danger" role="alert">
	{{m}}
	</div>
	% end
            
		<form method="POST" action="/upload" enctype="multipart/form-data"><div class="form-group">
			<label for="formGroupCategoryInput">Category</label>
			<input type="text" placeholder="Enter Category" name="category"><br><br>
            <label>Description</label>
			<input type="text" placeholder="Enter Description" name="description">
		</div>
			<div class="form-group">
			<label for="formGroupFileInput">Select File</label>
			<input type="file" class=".." placeholder="Select File"name="file_upload">
		</div>
			<button type="submit" class="btn btn-success">Submit</button>
		</form>
		
        <div class="navi" style="margin-top:38px">
			<a href="https://www.facebook.com"><img src="https://learntechno.s3.amazonaws.com/facebook.png" class="iconimg" alt="facebook"/></a>
			<a href="https://www.youtube.com"><img src="https://learntechno.s3.amazonaws.com/youtube.png" class="iconimg" alt="youtube"/></a>
			<a href="https://www.twitter.com"><img src="https://learntechno.s3.amazonaws.com/twitter.png" class="iconimg" alt="twitter"/></a>	
			<h6 class="leereplatz">Copyright &copy; 2020 learntech, Inc.</h6>
		</div>   
    </body>         
</html>
