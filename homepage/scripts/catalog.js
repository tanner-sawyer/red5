$(function() {
	$('#search_btn').on('click', function() {
		var search = $('#search_input').val();

		$('tr td.asset_code').each(function() {
			if ($(this).text().toUpperCase() == search.toUpperCase()) 
			{
				$(this).parent().show();
			}
			else if(search.length < 1)
			{
				$('tr').show();
			}
			else{
				$(this).parent().hide();
			}
		})
	})
})