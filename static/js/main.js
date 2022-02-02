$(document).ready(function() {	

	//block1

	$('.main__left button, .block17__header .button1').click(function() {
		var destination = $('.block7').offset().top;
		$('html, body').animate({ scrollTop: destination}, 500);
	})

	$('.main__nav__el-contacts').click(function (e) {
		e.preventDefault()
		var destination = $('.block8').offset().top;
		$('html, body').animate({ scrollTop: destination}, 500);
    })

	//block1 end

	//block2

	if ($('.block2__main-slider').length) {

		var galleryThumbs = new Swiper('.block2__thumbs', {
		      spaceBetween: 20,
		      slidesPerView: 3,
		      loop: true,
		      loopedSlides: 5, //looped slides should be the same
		      watchSlidesVisibility: true,
		      watchSlidesProgress: true,
		      slideToClickedSlide: true,
		    });
		    var galleryTop = new Swiper('.block2__main-slider', {
		      loop:true,
		      loopedSlides: 5,
		      thumbs: {
		        swiper: galleryThumbs,
		      },
		    });

			galleryTop.controller.control = galleryThumbs;
			galleryThumbs.controller.control = galleryTop;

	}

	//block4

	$('.block4__tab').each(function(e) {
		$(this).attr('data-block4', e)
	})
	$('.block4__item').each(function(e) {
		$(this).attr('data-block4', e)
	})
	$('.block4__tab').click(function() {
		if (!$(this).is('.block4__tab-active')) {
			$('.block4__tab').removeClass('block4__tab-active')
			$(this).addClass('block4__tab-active')

			var e = $(this).data('block4')
			$('.block4__item').removeClass('block4__item-active')
				$('.block4__item[data-block4='+e+']').addClass('block4__item-active')
		}
	})

	//block4 end


	//block11

	$('.block11 .block11__tab').each(function(e) {
		$(this).attr('data-block11', e)
	})
	$('.block11__item').each(function(e) {
		$(this).attr('data-block11', e)
	})
	$('.block11 .block11__tab').click(function() {
		if (!$(this).is('.block11__tab-active')) {
			$('.block11__tab').removeClass('block11__tab-active')
			$(this).addClass('block11__tab-active')

			var e = $(this).data('block11')
			$('.block11__item').removeClass('block11__item-active')
			$('.block11__item[data-block11='+e+']').addClass('block11__item-active')
			init_block11_slider(e)
		}
	})

	init_block11_slider(0)

	function init_block11_slider(el) {

		if ($('.block11').length) {

			var galleryThumbs = new Swiper('.block11__item[data-block11="'+el+'"] .block11__thumbs-slider', {
		      spaceBetween: 10,
		      slidesPerView: 3,
		      loop: true,
		      loopedSlides: 5, //looped slides should be the same
		      watchSlidesVisibility: true,
		      watchSlidesProgress: true,
		      slideToClickedSlide: true,
		      direction: 'vertical',
		      breakpoints: {
		      	750: {
		      		direction: 'horizontal'
		      	}
		      }
		    });
		    var galleryTop = new Swiper('.block11__item[data-block11="'+el+'"] .block11__main-slider', {
		      loop:true,
		      loopedSlides: 5,
		      thumbs: {
		        swiper: galleryThumbs,
		      },
		    });

			galleryTop.controller.control = galleryThumbs;
			galleryThumbs.controller.control = galleryTop;

		}

	}

	//block11 end


	//block14

	$('.block14__tab').each(function(e) {
		$(this).attr('data-block14', e)
	})
	$('.block14__item').each(function(e) {
		$(this).attr('data-block14', e)
	})
	$('.block14__tab').click(function() {
		if (!$(this).is('.block11__tab-active')) {
			$('.block14__tab').removeClass('block11__tab-active')
			$(this).addClass('block11__tab-active')

			var e = $(this).data('block14')
			$('.block14__item').removeClass('block14__item-active')
			$('.block14__item[data-block14='+e+']').addClass('block14__item-active')
		}
	})

	//block14 end


	//block20

	$('.block20__slider').owlCarousel({
		items: 1,
		touchDrag: false,
		mouseDrag: false,
		autoHeight: false,
		animateOut: 'fadeOut',
		onTranslated : block20_tabs
	})

	$('.block20__next').click(function(){
		if ($(this).data('step') == 2 &&
			($('.block20__step2 input[name="name"]').val() == '' ||
			$('.block20__step2 input[name="phone"]').val() == '' ||
			$('.block20__step2 input[name="email"]').val() == '' ||
				($('.block20__step2 input[name="delivery"]')[1].checked == true &&
					(
						$('.block20__step2 input[name="delivery_date"]').val() == '' ||
						$('.block20__step2 input[name="delivery_time"]').val() == '' ||
						$('.block20__step2 input[name="delivery_address"]').val() == ''
					)))) {
			var input_names = ['name', 'phone', 'email']
			if ($('.block20__step2 input[name="delivery"]')[1].checked == true) {
				input_names = input_names.concat(['delivery_address', 'delivery_time', 'delivery_date'])
			}
			$('.block20__step2 input').each(function (e) {
				if (input_names.includes($(this).attr('name')) && $(this).val() == '') {
					$(this).addClass('validation-error')
                }
            })
            var destination = $('.block20').offset().top;
            $('html, body').animate({scrollTop: destination}, 500);
            return false
		} else {
            $('.block20__slider').trigger('next.owl.carousel')
            var destination = $('.block20').offset().top;
            $('html, body').animate({scrollTop: destination}, 500);
        }
    })

	$('.block20__prev').click(function(){
    	$('.block20__slider').trigger('prev.owl.carousel')
    	var destination = $('.block20').offset().top;
		$('html, body').animate({ scrollTop: destination}, 500);
    })

    function block20_tabs(event) {
		var i = event.item.index
		$('.block20__tab').removeClass('block20__tab-active')
		$('.block20__tab').removeClass('block20__tab-completed')
		$('.block20__tab[data-block20-tab='+i+']').addClass('block20__tab-active')
		for(var index = 0; index<i; index++) {
			$('.block20__tab[data-block20-tab='+index+']').addClass('block20__tab-completed')
		}
	}

	$('.block20__step2 .block20__next').click(function (e) {
		e.preventDefault()
		$('.block20__step3 input[name=name]').val($('.block20__step2 input[name=name]').val())
		$('.block20__step3 input[name=email]').val($('.block20__step2 input[name=email]').val())
		$('.block20__step3 input[name=phone]').val($('.block20__step2 input[name=phone]').val())
		$('.block20__step3 input[name=company_name]').val($('.block20__step2 input[name=company_name]').val())
		$('.block20__step3 textarea[name=text]').val($('.block20__step2 textarea[name=text]').val())
		if ($('.block20__step2 input[name="delivery"]:checked').val() == 'Самовывоз') {
			$('.block20__step2 input[name="order_delivery"]').val('Самовывоз')
			$('.block20__step3 p').text('Вы выбрали самовывоз. Адрес: Каменск-Уральский, ул. Заводская, 9/8')
		} else {
			var address = $('.block20__step2 input[name=delivery_address]').val()
			var date = $('.block20__step2 input[name=delivery_date]').val()
			var time = $('.block20__step2 input[name=delivery_time]').val()
			var t = `Адрес доставки: ${address}. Дата: ${date}. Время: ${time}`
			$('.block20__step2 input[name="order_delivery"]').val(t)
			$('.block20__step3 p').text(t)
		}

		var a = $('.block20__step2').attr('action')
		var data = $('.block20__step2').serialize()
		$.ajax({
            type: "POST",
            url: a,
            data: data,
            success: function (data) {
            	cart_step3_update(data)
            }
    	})
    })
	$('.block20__step2 .block20__prev').click(function (e) {
		e.preventDefault()
    })

	function cart_step3_update(data) {
        for (let key in data.products) {
            var elem = `
				<div class="block17__tr">
					<div class="block17__cell b17-w8 block18__cell">
						<span>${data['products'][key]['name']}</span>
					</div>
					<div class="block17__cell b17-w9 block18__cell">
						<span>
							<span class='price'>${data['products'][key]['price_per_item']} р</span>
							<br>в т.ч. 20 % НДС
						</span>
					</div>
					<div class="block17__cell b17-w10 block18__cell">
						<div class="block18__cell__select">
							<select name="weight" disabled>
								<option>${data['products'][key]['quantity']}</option>
							</select>
							<select name="units" disabled>
								<option>кг</option>
								<option>м</option>
							</select>
						</div>
					</div>
					<div class="block17__cell b17-w12 block18__cell"><span><span class='price'>${data['products'][key]['total_price']} р</span></span></div>
					<div class="block17__cell b17-w13 block18__cell block20__delete">
						<img src="/static/img/icons/delete.png" alt=""/>
					</div>
				</div>
			`
			$('.block20__step3__body').append(elem)
        }
		$('.block20__step3__checkout .block20__checkout__info:first .text span').text(data['product_len'])
		$('.block20__step3__checkout .block20__checkout__info:nth-child(2) .text span').text(data['order_total_price']+' р')
	}

	$('.order-final').click(function () {
		$.ajax({
            type: "POST",
            url: '/cart/send_application/',
            data: '',
            success: function (data) {
				$('.block17__table-outer, .block20__tabs, .section__title').hide()
				$('.block20__thank').show()
				var destination = $('.block20').offset().top;
				$('html, body').animate({ scrollTop: destination}, 500);
				yaCounter54182878.reachGoal('g4')
            }
    	})
    })

	//block20 end


	//popups

	$('.callback-button').click(function(){
		document.body.style.overflow = 'hidden'
		$('.layer').fadeIn(300)
		$('.callback-popup').fadeIn(500)
	})

    $('.block17__header .button2').click(function() {
		document.body.style.overflow = 'hidden'
		$('.layer').fadeIn(300)
		$('.condition-popup').fadeIn(500)
	})

	$('.layer').click(function(e){
		if ($(this).has(e.target).length === 0) {
			document.body.style.overflow = 'scroll';
			$('.layer').fadeOut(300)
			$('.popup').fadeOut(300)
			$('.thank').fadeOut(300)
		}
	})
	$('.layer__close').click(function(){
		document.body.style.overflow = 'scroll';
		$('.layer').fadeOut(300)
		$('.popup').fadeOut(300)
		$('.thank').fadeOut(300)
	})

	//popups end


	//send forms

	$('.block7__form').submit(function (e) {
		e.preventDefault()
		var a = $(this);
		var action = $(this).attr('action')
		$.ajax({
            type: "POST",
            url: action,
            data: a.serialize(),
            success: function (data) {
                $('.layer').fadeIn(300)
				$('.popup').fadeOut(100)
				setTimeout(function () {
					$('.block20__thank.popup').fadeIn(300)
                }, 100)

				if (a.find('input[name=type]').val() == 'Заявка на обратный звонок') {
                	yaCounter54182878.reachGoal('g1')
                } else if (a.find('input[name=type]').val() == 'Заявка на КП / О компании') {
                	yaCounter54182878.reachGoal('g2')
                } else if (a.find('input[name=type]').val() == 'Заявка на КП / Продукция') {
                	yaCounter54182878.reachGoal('g3')
                } else if (a.find('input[name=type]').val() == 'Заявка на КП / Услуги') {
                	yaCounter54182878.reachGoal('g5')
                }
            }
    	})
    })

	//send forms end


	/* mobile */

	block4_tabs()
	$(window).on('resize', block4_tabs)

	function block4_tabs() {
		if ($(window).width() < 1200) {
			$('.block4__tabs').addClass('owl-carousel')
			$('.block4__tabs').owlCarousel({
				items: 1,
				addClassActive: true,
				margin: 7
		    })
		} else {
			$('.block4__tabs').removeClass('owl-carousel')
			$('.block4__tabs').trigger('destroy.owl.carousel');
		}
	}

	block5__flex()
	$(window).on('resize', block5__flex)

	function block5__flex() {
		if ($(window).width() < 750) {
			$('.block5__flex').addClass('owl-carousel')
			$('.block5__flex').owlCarousel({
				items: 1,
				addClassActive: true,
				margin: 30
		    })
		} else {
			$('.block5__flex').removeClass('owl-carousel')
			$('.block5__flex').trigger('destroy.owl.carousel');
		}
	}

	block11__tabs()
	$(window).on('resize', block11__tabs)

	function block11__tabs() {
		if ($(window).width() < 1200) {
			$('.block11__tabs').addClass('owl-carousel')
			$('.block11__tabs').owlCarousel({
				items: 1,
				addClassActive: true,
				margin: 7
		    })
		} else {
			$('.block11__tabs').removeClass('owl-carousel')
			$('.block11__tabs').trigger('destroy.owl.carousel');
		}
	}

	$('.m-menu-btn').click(function(){
		$('.mobile-menu').addClass('mobile-menu-active')
	})
	$('.mobile-menu .main__nav__el, .close-menu').click(function() {
		$('.mobile-menu').removeClass('mobile-menu-active')
	})

	//other

	$('.select-wrapper select').niceSelect()

	//block18__cell__select price change

	$(document).on('change', '.block18__cell__select select', function () {
        var product_block = $(this).parents('.block17__tr')
        var val = $(this).val()
        var id = product_block.attr('id')
        $.ajax({
            type: "POST",
            url: '/shop/get_price/',
            data: {'units': val, 'id': id},
            success: function (data) {
                product_block.children('.block18__price').children('span').children('.price')
                    .html(data+' р')
                    .data('price', data)
                block18_calculate_price(id)
                product_block.children('.block18__buy').children('form').children('input[name=product_units]').val(val)
            }
        })
        return false;
    })

    $(document).on('change', '.block18__quanity input', function () {
        var parent = $(this).parents('.block18__cell__select').parents('.block18__quanity').parents('.block17__tr')
		if ($(this).val() > 0) {
            var id = parent.attr('id')
            block18_calculate_price(id)
        } else {
			$(this).val(1)
		}
		parent.children('.block18__buy').children('form').children('input[name=product_quantity]').val($(this).val())
    })

	function block18_calculate_price(id) {
		var parent = $('.block17__tr#'+id)
		var price_per_unit = parent.children('.block18__price').children('span').children('.price').data('price')
        parent.children('.block18__buy').children('form').children('input[name=product_price]').val(price_per_unit)
		var quanity = parent.children('.block18__quanity').children('.block18__cell__select').children('input').val()
		var total_price = price_per_unit*quanity
		parent.children('.block18__total-price').children('span').children('.price').html(total_price+' р')
    }

	//block18__cell__select price change end


	//block18 ajax data get

    $(document).on('click', '.block18__nav a.page-link', function (e) {
		e.preventDefault()
		var page = $(this).attr('href')
        var sort_name = $('.block17__body').data('sort_name')
        var sort = $('.block17__body').data('sort')
        var materials = $('.block18__filters select[name=materials]').val()
        var marks = $('.block18__filters select[name=marks]').val()
        var thickness = $('.block18__filters select[name=thickness]').val()
        var is_sale = $('.block17__body').data('sale')
		$.ajax({
            type: "POST",
            url: '/shop/',
            data: {
                'page': page,
                'sort_name': sort_name,
                'sort': sort,
                'materials': materials,
                'marks': marks,
                'thickness': thickness,
                'is_sale': is_sale
            },
            success: function (data) {
                block18_update(data)
            }
    	})
    })

	//block18 ajax data get end


    //block18 sort

    $('.block18__sort select').change(function () {
        var name = $(this).attr('name')
        var d = $(this)[0].options[$(this)[0].selectedIndex].value
        var materials = $('.block18__filters select[name=materials]').val()
        var marks = $('.block18__filters select[name=marks]').val()
        var thickness = $('.block18__filters select[name=thickness]').val()
        var is_sale = $('.block17__body').data('sale')
        if (name == 'thickness') {
            $('.block18__sort select[name="price_per_kilo"]')[0].selectedIndex = 0
            $('.block18__sort select[name="price_per_kilo"]').niceSelect('update')
        } else {
            $('.block18__sort select[name="thickness"]')[0].selectedIndex = 0
            $('.block18__sort select[name="thickness"]').niceSelect('update')
        }
        $.ajax({
            type: "POST",
            url: '/shop/',
            data: {
                'is_sale': is_sale,
                'sort_name': name,
                'sort': d,
                'materials': materials,
                'marks': marks,
                'thickness': thickness
            },
            success: function (data) {
                block18_update(data)
                $('.block17__body').data('sort_name', name)
                $('.block17__body').data('sort', d)
            }
        })
    })

    //block18 sort end

    //block18 filter

    $('.block18__filters').submit(function (e) {
        e.preventDefault()
        var sort_name = $('.block17__body').data('sort_name')
        var sort = $('.block17__body').data('sort')
        var materials = $('.block18__filters select[name=materials]').val()
        var marks = $('.block18__filters select[name=marks]').val()
        var thickness = $('.block18__filters select[name=thickness]').val()
        var is_sale = $('.block17__body').data('sale')
		$.ajax({
            type: "POST",
            url: '/shop/',
            data: {
                'is_sale': is_sale,
                'sort_name': sort_name,
                'sort': sort,
                'materials': materials,
                'marks': marks,
                'thickness': thickness
            },
            success: function (data) {
                block18_update(data)
                $('.block17__body').data('materials', materials)
                $('.block17__body').data('marks', marks)
                $('.block17__body').data('thickness', thickness)
            }
    	})
    })

    //block18 filter end

    //block18 sale filter

    $('.block18__sale-btn').click(function () {
        var is_sale = $('.block17__body').data('sale')
        var sort_name = $('.block17__body').data('sort_name')
        var sort = $('.block17__body').data('sort')
        var materials = $('.block18__filters select[name=materials]').val()
        var marks = $('.block18__filters select[name=marks]').val()
        var thickness = $('.block18__filters select[name=thickness]').val()
        if (!is_sale || is_sale=='normal') {
            is_sale = 'sale'
        } else {
            is_sale = 'normal'
        }
        $.ajax({
            type: "POST",
            url: '/shop/',
            data: {
                'is_sale': is_sale,
                'sort_name': sort_name,
                'sort': sort,
                'materials': materials,
                'marks': marks,
                'thickness': thickness
            },
            success: function (data) {
                block18_update(data)
                if (is_sale=='sale') {
                    $('.block18__sale-btn').text('показать продукцию')
                    $('.block17__body').data('sale', is_sale)
                } else {
                    $('.block18__sale-btn').text('распродажа со склада')
                    $('.block17__body').data('sale', is_sale)
                }
            }
    	})
    })

    //block18 sale filter end

    //block18 update func

    function block18_update(data) {
	    $('.block17__body').empty()
        for (let key in data.products) {
            let elem = `
                <div class="block17__tr" id="${data['products'][key]['id']}">
                    <div class="block17__cell b17-w8 block18__cell">
                        <span>${data['products'][key]['name']}</span>
                    </div>
                    <div class="block17__cell b17-w9 block18__cell block18__price">
                        <span>
                            <span class='price' data-price="${data['products'][key]['price']}">${data['products'][key]['price']} р</span>
                            <br>в т.ч. 20 % НДС
                        </span>
                    </div>
                    <div class="block17__cell b17-w10 block18__cell block18__quanity">
                        <div class="block18__cell__select">
                            <input type="number" name="weight" value="1" required>
                            <select name="units">
                                <option>кг</option>
                                <option>шт</option>
                            </select>
                        </div>
                    </div>
                    <div class="block17__cell b17-w12 block18__cell block18__total-price">
                        <span><span class='price'>${data['products'][key]['price']} р</span></span>
                    </div>
                    <div class="block17__cell b17-w13 block18__cell block18__buy">
                        <form action="${data['add_cart_url']}" method="post">
                            <input type="hidden" name="product_id" value="${data['products'][key]['id']}">
                            <input type="hidden" name="product_units" value="кг">
                            <input type="hidden" name="product_quantity" value="1">
                            <button class="block18__buy-btn">купить</button>
                        </form>
                    </div>
                </div>
            `
            $('.block17__body').append(elem)
        }

        $('.pagination').empty()
        $('.pagination').append(data['pagination'])
    }

    //block18 update func end


    //basket push items from shop page

    toastr.options = {
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": false,
      "positionClass": "toast-top-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "3000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
    }

    $(document).on('submit', '.block18__buy form', function (e) {
        e.preventDefault()
        var d = $(this).serialize()
        var url = $(this).attr('action')
        $.ajax({
            type: "POST",
            url: url,
            data: d,
            success: function (data) {
                var l = data.product_len
                $('.cart-num span').text(l)
                toastr.success('Товар добавлен в корзину!')
            }
    	})
    })

    //basket push items form shop page end


    //basket remove items

    $(document).on('submit', '.block20__delete form', function (e) {
        e.preventDefault()
        var d = $(this)
        var url = $(this).attr('action')
        $.ajax({
            type: "POST",
            url: url,
            data: d.serialize(),
            success: function (data) {
                d.parents('.block20__delete').parents('.block17__tr').remove()
                $('.block20__checkout__info:first span').text(data.product_len)
                $('.block20__checkout__info:nth-child(2) span').text(data.total_price+' руб')
                toastr.success('Товар удален из корзины!')
            }
    	})
    })

    //basket remove items end


    //basket quantity change

    $('.block20__quantity').change(function () {
        var q = $(this).val()
        var parent = $(this).parents('.block18__cell__select').parents('.block18__cell').parents('.block17__tr')
		if ($(this).val() > 0) {
            var id = parent.attr('id')
            $.ajax({
                type: "POST",
                url: 'cart/change_quantity/',
                data: {
                    'product_id': id,
                    'product_quantity': q,
                },
                success: function (data) {
                    parent.children('.block20__product__total').children('span').children('.price').text(data.product_total)
                    $('.block20__checkout__info:first span').text(data.product_len)
                    $('.block20__checkout__info:nth-child(2) span').text(data.total_price+' руб')
                }
            })
        } else {
			$(this).val(1)
		}
    })

    //basket quantity change end


})