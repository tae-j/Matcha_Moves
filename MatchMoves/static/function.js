function loadPopularItems() {
    fetch('/get_popular_items')
        .then(response => response.json())
        .then(items => {
            const container = document.getElementById('popular-items');
            items.forEach(item => {
                const itemDiv = document.createElement('div');
                itemDiv.className = 'col-md-4 mb-3';
                itemDiv.innerHTML = `
                    <div class="card">
                        <a href="/view/${item.id}">
                            <img src="${item.image}" class="card-img-top" alt="${item.name}">
                        </a>
                        <div class="card-body">
                            <h5 class="card-title">${item.name}</h5>
                            <span class = "drink"> Specialty Drink: ${item.matcha[1]}</span> 
                        </div>
                    </div>
                `;
                container.appendChild(itemDiv);
            });
        })
        .catch(error => console.error('Error loading popular items:', error));
}



// Search functionality
$(document).ready(function() {
    $('#search-form').on('submit', function(e) {
        e.preventDefault();
    
        var $searchInput = $('#search-input');
        var query = $searchInput.val().trim();
        
        if (query === '') {
            $searchInput.val('');
            $searchInput.focus();

            return false;
        }
        
        window.location.href = '/search?q=' + encodeURIComponent(query);
    });

    function highlightSubstring(query) {
        const regex = new RegExp(query, 'gi');  // Create case-insensitive regex
        $('.match-text').each(function() {
            const text = $(this).text();
            const highlightedText = text.replace(regex, function(match) {
                return '<span class="highlight">' + match + '</span>';
            });
            $(this).html(highlightedText);  // Replace text with highlighted version
        });
    }


    // load popular items
    if (document.getElementById('popular-items')) {
        loadPopularItems();
    }

    $('#add-item-form').on('submit', function(e){
        e.preventDefault(); 


        const name = $('#name').val().trim();
        const image = $('#image').val().trim();
        const rating = $('#rating').val().trim();
        const address = $('#address').val().trim();
        const overview = $('#overview').val().trim();
        const matcha = $('#matcha').val().trim();
        const other = $('#other').val().trim(); 

            const errors = {};

            if (!name) errors['name'] = "Location Name is required.";
            if (!image) errors['image'] = "Image Link is required.";
            if (!rating || isNaN(parseFloat(rating))) errors['rating'] = "Rating must be a number.";
            if (!address) errors['address'] = "Location Address is required.";
            if (!overview) errors['overview'] = "Location Overview is required.";
            if (!matcha) errors['matcha'] = "Matcha drinks menu is required";
            if (!other) errors['other'] = "Other drinks is required";
    
            // If there are any errors, display them and stop the form submission
            if (Object.keys(errors).length > 0) {
                // Display errors for each field
                $('#name-error').text(errors.name || "");
                $('#image-error').text(errors.image || "");
                $('#rating-error').text(errors.rating || "");
                $('#address-error').text(errors.address || "");
                $('#overview-error').text(errors.overview || "");
                $('#matcha-error').text(errors.matcha || "");
                $('#other-error').text(errors.other || "");
                return;
            }

                    // If no errors, proceed with AJAX submission
        const formData = {
            name: name,
            image: image,
            rating: rating,
            address: address,
            overview: overview,
            matcha: matcha,
            other: other
        };

        $.ajax({
            type: 'POST',
            url: '/add',
            data: formData,
            success: function(response) {
                $('#success-message').show();
                $('#view-link').attr('href', '/view/' + response.item_id);
                $('#add-item-form').trigger('reset');
                $('#name').focus(); // Focus on the first input field

                const query = $('#search-input').val().trim().toLowerCase();  // Get the current search query
                if (query) {
                    highlightSubstring(query);  // Highlight substrings based on the search query
                }

            },
            error: function(response) {
                const errors = response.responseJSON.errors;
                if (errors.name) $('#name-error').text(errors.name);
                if (errors.image) $('#image-error').text(errors.image);
                if (errors.rating) $('#rating-error').text(errors.rating);
                if (errors.address) $('#address-error').text(errors.address);
                if (errors.overview) $('#overview-error').text(errors.overview);
                if(errors.matcha) $('#matcha-error').text(errors.matcha); 
                if(errors.other) $('#other-error').text(errors.other); 
            }
        }); 
    });


    //editing 
    $('#edit-item-form').submit(function(e){
        e.preventDefault(); 

        const itemId = $('#edit-item-form').data('item-id');


        const formData = {
            name: $('#name').val(),
            image: $('#image').val(),
            rating: $('#rating').val(),
            address: $('#address').val(),
            overview: $('#overview').val(),
            matcha: $('#matcha').val(),
            other: $('#other').val()
        };

        // Send the form data via AJAX POST
        $.ajax({
            type: 'POST',
            // url: '/edit/{{ item.id }}',  // Send the data to the /edit/<id> route
            url: '/edit/' + itemId,
            data: formData,
            success: function(response) {
                // Redirect to the view page if the update is successful
                // window.location.href = '/view/{{ item.id }}';
                window.location.href = '/view/' + itemId;
            },
            error: function(response) {
                // Display an error message if something goes wrong
                alert('There was an error saving the changes. Please try again.');
            }
        });
    });

 }); 