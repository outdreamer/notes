topics to cover for js:

- ideas:
	- you could always store numbers as fractions to avoid inaccuracies
	- you could convert code to the optimal language for a particular task type
	- rather than flex layouts, specify template items (table + modal layout) & content to fill them 
		<table-modal table-data="my_table_data" modal-content="my_modal_form_fields"/>
		- you wouldnt have to specify a submit button action because any request data received is fit to available functions,
		 and if it finds one that matches the input, it executes that
	- test automation:
		find expectations/assumptions:
		- possible vs. expected ranges of input values, output values, value checks, handled exceptions
		find intent:
		- missing conditions, value checks, processing, & exception handling
	- code optimization: 
		- replacing sub-optimal coding patterns with faster versions that dont change operations, within a language/version/dependency context
		- merging redundant logic (extra unnecessary checks or assignments, unnecessary variables)
- css 
	- animations
		@keyframes mymove {
		    from {top: 0px;}
		    to {top: 200px;}
		}
	- layout
		- Before the Flexbox Layout module, there were four layout modes:
		    - Block, for sections in a webpage
		    - Inline, for text
		    - Table, for two-dimensional table data
		    - Positioned, for explicit position of an element
		- display: inline* block flex grid table* list-item contents
		- float
			- The float property specifies how an element should float.
			- Absolutely positioned elements ignores the float property!
			- Elements after a floating element will flow around it
			- The clear property specifies on which sides of an element floating elements are not allowed to float.
			- To avoid this, use the clear property or the clearfix hack:
				.clearfix::after {
				  content: "";
				  clear: both;
				  display: table;
				}

		- flexbox
			- flex-container:
				display: flex;
				- flex-direction: column column-reverse row row-reverse;
				- flex-wrap: wrap nowrap(default) wrap-reverse;
				- flex-flow: row wrap; // property is a shorthand property for setting both the flex-direction and flex-wrap properties.
				- justify-content: flex-start(default) center flex-end space-between; //property is used to align the flex items, like centering them
				- align-items: flex-start(default) center flex-end stretch(default) baseline; //aligns items vertically, baseline aligns text baseline (lowest point)
				- align-content: space-between flex-start center flex-end space-around stretch(default); //aligns flex lines
			- tip: set both the justify-content and align-items properties to center, and the flex item will be perfectly centered
			- flex-container child items:
			    - order: 0; specify the index an item should appear at
			    - flex-grow: 0; specifies how much an item will grow relative to the other items
			    - flex-shrink 0; specifies how much an item will shrink relative to the other items
			    - flex-basis: 200px; specifies initial length of the item
			    - flex: 0 0 200px; a shorthand property for the flex-grow, flex-shrink, and flex-basis properties.
			    - align-self: flex-start(default) center flex-end stretch(default) baseline; 
			    	specifies alignment for the selected item inside the flexible container, overriding the container align-items property
	- media queries
		- Media queries can be used to check many things, such as:

		    - device/viewport width & height
		    - orientation (landscape/portrait for non-desktops)
		    - resolution
		    - supported types: all, print, screen, or speech

			- @media not|only screen and (max-width: 600px and|or|not ) {}
			- @media screen and (max-width: 900px) and (min-width: 600px), (min-width: 1100px) 

			 <link rel="stylesheet" media="screen and (min-width: 900px)" href="widescreen.css">

				any-hover 	Does any available input mechanism allow the user to hover over elements? (added in Media Queries Level 4)
				any-pointer 	Is any available input mechanism a pointing device, and if so, how accurate is it? (added in Media Queries Level 4)
				aspect-ratio 	The ratio between the width and the height of the viewport
				color 	The number of bits per color component for the output device
				color-gamut 	The approximate range of colors that are supported by the user agent and output device (added in Media Queries Level 4)
				color-index 	The number of colors the device can display
				grid 	Whether the device is a grid or bitmap
				height 	The viewport height
				hover 	Does the primary input mechanism allow the user to hover over elements? (added in Media Queries Level 4)
				inverted-colors 	Is the browser or underlying OS inverting colors? (added in Media Queries Level 4)
				light-level 	Current ambient light level (added in Media Queries Level 4)
				max-aspect-ratio 	The maximum ratio between the width and the height of the display area
				max-color 	The maximum number of bits per color component for the output device
				max-color-index 	The maximum number of colors the device can display
				max-height 	The maximum height of the display area, such as a browser window
				max-monochrome 	The maximum number of bits per "color" on a monochrome (greyscale) device
				max-resolution 	The maximum resolution of the device, using dpi or dpcm
				max-width 	The maximum width of the display area, such as a browser window
				min-aspect-ratio 	The minimum ratio between the width and the height of the display area
				min-color 	The minimum number of bits per color component for the output device
				min-color-index 	The minimum number of colors the device can display
				min-height 	The minimum height of the display area, such as a browser window
				min-monochrome 	The minimum number of bits per "color" on a monochrome (greyscale) device
				min-resolution 	The minimum resolution of the device, using dpi or dpcm
				min-width 	The minimum width of the display area, such as a browser window
				monochrome 	The number of bits per "color" on a monochrome (greyscale) device
				orientation 	The orientation of the viewport (landscape or portrait mode)
				overflow-block 	How does the output device handle content that overflows the viewport along the block axis (added in Media Queries Level 4)
				overflow-inline 	Can content that overflows the viewport along the inline axis be scrolled (added in Media Queries Level 4)
				pointer 	Is the primary input mechanism a pointing device, and if so, how accurate is it? (added in Media Queries Level 4)
				resolution 	The resolution of the output device, using dpi or dpcm
				scan 	The scanning process of the output device
				scripting 	Is scripting (e.g. JavaScript) available? (added in Media Queries Level 4)
				update 	How quickly can the output device modify the appearance of the content (added in Media Queries Level 4)
				width 	The viewport width

		- The viewport is the visible area of a web page
			<meta name="viewport" content="width=device-width, initial-scale=1.0">

	- responsive:
		- box-sizing: border-box; makes sure padding & border is included in height & width
	- sass features
	    - Preprocessing
	    	- static: sass input.scss output.css
	    	- dynamic: sass --watch input.scss output.css
	    - Variables
	    	- used to store values that are reused in the scss 
		    	$font-stack:    Helvetica, sans-serif;
				body {
				  font: 100% $font-stack;
				}
	    - Nesting
	    	- allows mimicking the html structure within css, to share properties between parent & child elements
	    - Partials
	    	- a Sass file named with a leading underscore that is not included in the generated file but can be imported & reused to other files
	    - Import
	    	- Sass builds on the current CSS @import but instead of requiring an HTTP request, 
	    	except Sass combines imported files & serves a single CSS file to the web browser
	    	@import 'reset';

	    - Mixins: group properties, optionally passing in a variable 
		    @mixin transform($property) {
			  -webkit-transform: $property;
			  -ms-transform: $property;
			  transform: $property;
			}
			.box { @include transform(rotate(30deg)); }

	    - Inheritance
	    	- an alternative to nesting that allows sharing attributes
		    	%message-shared {
				  border: 1px solid #ccc;
				}
				.success {
				  @extend %message-shared;
				  border-color: green;
				}

	    - Operators
			article[role="main"] {
			  float: left;
			  width: 600px / 960px * 100%;
			}

- js standard features:
	- if (typeof myObj === "undefined")  
	- if (typeof myObj !== "undefined" && myObj !== null)  
	- js optimization methods: https://www.w3schools.com/js/js_performance.asp
		- write smaller DOMs
		- reduce loop operations 
		- reduce unnecessary variables
		- reduce DOM access queries by defining dom in a variable
		- delay js loading by putting scripts at bottom & using defer="true" in script tag for external scripts
		- delay js loading by loading scripts in window.onload:
		<script>
			window.onload = function() {
			  var element = document.createElement("script");
			  element.src = "myScript.js";
			  document.body.appendChild(element);
			};
		</script> 
		- render order:
			Render order is determined by the order in which you append elements to the document; elements are drawn in document traversal order.

	- event bubbling & delegation:
		- always assign to the parent element and check which child element the event was triggered with using e.target
	- closures
	- promises 
	- iterator/generator
	- let
- js strict mode:
	- doesnt allow with keyword bc it interferes with speed & scopes
- js validation:
	- jslint (what mistakes does it prevent, what configurations)
- js framework concepts:
	- angular 
		- component lifecycle
		- services
		- observables
- webkit: Apples browser engine used in safari, descended from KDEs implementation of a browser engine & javascript, under BSD license
	- webcore: originally the KHTML browser engine, a component of webkit forked for use in chrome as Blink
	- javascriptcore: originally the KJS javascript implementation, a webkit component available with gnu lgpl license, along with webcore
- server-side js implementations (particularly node/v8)
	- jscript: microsoft javascript engine
	- rhino: browser engine written in java from mozilla
	- spidermonkey: 
		- first browser engine providing javascript support for firefox, written in c from mozilla,
		- doesnt provide host environments like DOM (Gecko provides this)
	- gecko: Mozilla Firefox browser/layout/rendering engine, written in C++ & javascript
	- quantum: Firefox improvement of gecko including stable parts of servo
	- servo: firefox project to improve parallel processing & concurrency & reducing memory safety vulns, written in Rust
	- node: 
		- Node.js is planned to become VM neutral, most Node.js instances are based on the V8 JavaScript engine
		- an asynchronous event driven JavaScript runtime, designed to build scalable network applications, in which connections can be handled concurrently
		- Almost no function in Node directly performs I/O (system disk & network), so the process never blocks/locks	
	- v8: 
		- used in Chrome and node.js runtime environment, using Ignition (the interpreter) and TurboFan (the optimizing compiler), 
			using Blink as its browser engine
		- compiles JavaScript directly to native machine code before executing it, 
			instead of more traditional techniques such as interpreting bytecode,
			or compiling the whole program to machine code and executing it from a filesystem.
		- The compiled code is additionally optimized (and re-optimized) dynamically at runtime, based on heuristics of the codes execution profile. 
		- Optimization techniques used include inlining, elision of expensive runtime properties, and inline caching. 
		- The garbage collector is a generational incremental collector.[7]
- v8 optimization:
	https://community.risingstack.com/how-to-find-node-js-performance-optimization-killers/
- node performance:
	- overview: https://nodejs.org/en/about/
	- concurrency: https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/
- browser testing tools
	- UI testing:
		- crossbrowsertesting.com & browserstack both use real devices rather than emulators
	- site optimization testing:
		- web page analyzer, gtmetrix, website pulse, pingdom tools
		- google.com/websiteoptimizer, Yslow & google pagespeed insights
		- https://www.webpagetest.org
		https://www.sitepoint.com/tools-testing-website-performance/

- js testing 
	- phantom js: headless event mimicking in javascript allowing screenshots 
	- selenium: 
- ecmascript features
	- es5

	- es6 
		- added export & export default keywords 
		- use import keyword rather than require function
		- arrows functions: const functionName = (params) => {}
- webpack: 
- scaling/performance
- computational complexity of common operations in various implementations
	o(1)
		Array.push() - adds an element & gives it an index that’s 1 greater than the index of the last element in the array
		Array.pop() - removes element from end of array 

	o(n)
		Array.unshift() - adds element to beginning
		Array.shift() - removes element from beginning 
		Array.splice(index) - worst case scenario of removing an item from the beginning
		Array.filter()
		Array.map()
		Array.find()
		Array.findIndex()
		Array.reduce()
		Array.forEach() 

	o(n + k)
		Array.concat()

- channels, sockets, queues, streams

- multi-threading
	- can mimic concurrency using scheduling functions like setTimeout, or delaying functionality with promises

- promise:
	- The ES6 promises are better then callback because it allows us to distinguish easily between a success and error so we don’t have to check again for things in our callback function.

	- A Promise handles a single event when an async operation completes or fails. 
		- there are Promise libraries out there that support cancellation, but ES6 Promise doesnt so far.
	- An Observable is like a Stream (in many languages)
		- allows to pass zero or more events where the callback is called for each event
		- is cancelable, by canceling the subscription of an observable
		- in contrast a promise will finish its execution even if you dont need it to
		- Observables provide operators like map, forEach, reduce, etc

		- create a dependency flow that handles success & error conditions of dependent functions
		- catch() is called when any exception is thrown from the Promise constructor callback.
		- promise.status: pending, fulfilled, rejected 
		- promise argument functions: resolve (with data), reject (with error)
		- If promise was fulfilled, the success callback resolve() is called with the actual data you passed to resolve()
		- If the promise was rejected, the failure callback reject() is called with whatever Error object you passed to reject()

		const promise = new Promise((resolve, reject) => {
		  const request = new XMLHttpRequest();
		  request.open('GET', url);
		  request.onload = () => {
		    if (request.status === 200) {
		      resolve(request.response); // we got data here, so resolve the Promise
		    } else {
		      reject(Error(request.statusText)); // status is not 200 OK, so reject
		    }
		  };
		  request.onerror = () => {
		    reject(Error('Error fetching data.')); // error occurred, reject the  Promise
		  };
		  request.send(); // send the request
		});

		promise.then((data) => {
		  console.log('Got data! promise fulfilled', data);
		}).catch((error) => {
		  console.log('Error! promise rejected', error);
		});

		search(term:string) {
		  let promise = new Promise((resolve, reject) => {
		  	//get returns an Observable, which we convert to a promise
		    this.http.get(apiURL)
		      .toPromise()
		      .then(
		        res => { // Success
		          console.log(res.json());
		          this.results = res.json().results.map(item => {
	                  return new SearchItem(
	                      item.property1,
	                      item.property2
	                  );
	              });
	              // this.results = res.json().results;
		          resolve();
		        },
		        msg => { // Error
		          reject(msg);
		        }
		      );
		  });
		  return promise;
		}
		<ul class="list-group">
		  <li class="list-group-item"
		      *ngFor="let track of myService.results">
		    <img src="{{track.property1}}">
		    <a target="_blank" href="{{track.property2}}">{{ track.property3 }}
		    </a>
		  </li>
		</ul>

- Angular snippets:

	import 'rxjs/add/operator/toPromise';
	@NgModule({
	  imports: [
	    BrowserModule,
	    HttpModule,
	  ],
	  declarations: [AppComponent],
	  bootstrap: [AppComponent],
	  providers: [SearchService]
	})
	class AppModule { }

	class SearchItem {
	  constructor(
	    public property1: string,
	    public property2: string
	  ) {}
	}

	@Injectable()
	export class SearchService {
		constructor(private http: HttpClient) {)

	)

	class AppComponent {
	  private loading: boolean = false;
	  results: SearchItem[];
	  constructor(private myService:SearchService) { }

	  doSearch(term:string) {
	  	this.loading = true;
	    this.myService.search(term).then( () => this.loading = false);
	  }
	}

