$(function(){
    
    var companyList_size = $('.CompanyCard').length; // total length of cards
    var renderCardSize = 6; // Number of Cards to be shown

    // active selection Tracker
    var activeLocation = [];
    var activeScale = [];
    var activeTechnology = [];


    //------------------- Randomization of Cards ----------------

    function randomizeCards(){
        
        var $companyCardContainer = $('.CompanyCardContainer');
        var $cardArr = $companyCardContainer.children('.Indexed');
        
        $cardArr.sort(function(){
            return 0.5 - Math.random(); // Randomization Function has to be improvised.
        }); 
        
        $cardArr.appendTo($companyCardContainer);
        
        // append Show more buttons as well
        $('#showMoreBtn').detach().appendTo('.CompanyCardContainer')
        $('#showLessBtn').detach().appendTo('.CompanyCardContainer')
    }

    //--------------------- End Randomization ---------------------


    // ------------------ Card Render Mechanism --------------------

    function renderCompanyCards() { // Render the Limited Cards

        $('.CompanyCard').slice(0, renderCardSize).show();
        if(renderCardSize < companyList_size){
            $('#showMoreBtn').show()
            $('#showLessBtn').hide()
        } else {
            $('#showMoreBtn').hide()
            $('#showLessBtn').show()
        }
    }

    $('#showMoreBtn').click(() => {
        if(renderCardSize < companyList_size){
            renderCardSize += 6;
            renderCompanyCards();
        }
    })

    $('#showLessBtn').click(() => {
        if(renderCardSize > 6){
            renderCardSize -= 6;
            $('.CompanyCard').hide();
            renderCompanyCards();
        }
    })
    // ------------------End of  Card Render Mechanism --------------------

    // Method to make a POST request to fetch a New Data
    function fetchData(){
        console.log("Tried to make a request");
        // Send Request to fetch Data with Updated Filters
        // $.ajax({
        //     url: '/dummyURL',
        //     method: 'POST',
        //     data: {
        //         // data of array
        //         'location[]': activeLocation,
        //         'scale[]': activeScale,
        //         'technology': activeTechnology
        //     },
        //     success: (responseData) => {
        //         console.log("POST Request sent with data : " + responseData)
        //         renderCardSize = 6; // setting default value of X
        //     }
        // })
        console.log(activeLocation, activeScale, activeTechnology);
    }

    //---------- For Location Tag ALTER -------------

    $('#tagLocation').click((e) => {

        // type check if it is an a element
        if(e.target.tagName == "A"){

            var tagindx = activeLocation.indexOf(e.target.id);
            
            if(tagindx != -1){
                activeLocation.splice(tagindx, 1);
                e.target.classList.remove("active");
            } else {
                activeLocation.push(e.target.id);
                e.target.classList.add("active");
            }
            
            fetchData();
        }
    });

    //---------- For Scale Tag ALTER -------------

    $('#tagScale').click((e) => {

        // type check if it is an a element
        if(e.target.tagName == "A"){

            var tagindx = activeScale.indexOf(e.target.id);

            if(tagindx != -1){
                activeScale.splice(tagindx, 1);
                e.target.classList.remove("active");
            } else {
                activeScale.push(e.target.id);
                e.target.classList.add("active");
            }

            fetchData();
        }
    });

    //---------- For Technology Tag ALTER -------------

    $('#tagTechnology').click((e) => {

        // type check if it is an a element
        if(e.target.tagName == "A"){

            var tagindx = activeTechnology.indexOf(e.target.id);

            if(tagindx != -1){
                activeTechnology.splice(tagindx, 1);
                e.target.classList.remove("active");
            } else {
                activeTechnology.push(e.target.id);
                e.target.classList.add("active");
            }

            fetchData();
        }
    });

    // On load Function
    (function(){
        // console.log($('.CompanyCard'))
        randomizeCards()
        $('.CompanyCard').hide();
        renderCompanyCards();
    })();
})