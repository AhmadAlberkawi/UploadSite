% include('header.tpl', title=name)
% for item in items:
  
	<div class="col-md-4">
		<div class="thumbnail">
			<a href="https://learntechno.s3.amazonaws.com/{{item.get('filename')}}">
					<img width="100%" src="https://learntechno.s3.amazonaws.com/{{item.get('filename')}}">
				<div class="caption">
					<p>{{item.get('description')}}</p>
				</div>
			</a>
		</div>
   </div>
   
% end
% include('footer.tpl')
