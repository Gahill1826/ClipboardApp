<template>
	<div class="filters">
		<button class="accordion-button" @click="open">Filter Results</button>						
		<div class="accordion-panel">
			<div class="form-group">
				<label for="locationFilter">Where</label>
				<input type="text" class="form-control" id="locationFilter" placeholder="Zip / Neighborhood">
			</div>

			<div class="form-group">
				<label for="locationFilter">Distance (Miles)</label>
				<select class="form-control" id="distanceFilter">
					<option value="5">5</option>
					<option value="10" selected>10</option>
					<option value="25">25</option>
					<option value="50">50</option>
					<option value="100">100</option>
				</select>
			</div>

			<div class="form-group">
				<label for="fromDatePicker">From</label>
				<datepicker :value="state.date" name="fromDatePicker" wrapper-class="datepicker" class="datepicker"></datepicker>
			</div>

			<div class="form-group">
				<label for="toDatePicker">To</label>
				<datepicker :value="state.date" name="toDatePicker" wrapper-class="datepicker" class="datepicker"></datepicker>
			</div>
		</div>
			
		<button class="accordion-button" @click="open">Category</button>
		<div class="accordion-panel">
			<div class="form-group">
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="environmentCheck">
					<label class="form-check-label" for="environmentCheck">
						Environment
					</label>
				</div>
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="homelessnessCheck">
					<label class="form-check-label" for="homelessnessCheck">
						Homelessness
					</label>
				</div>
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="hospitalsCheck">
					<label class="form-check-label" for="hospitalsCheck">
						Hospitals
					</label>
				</div>
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="hungerCheck">
					<label class="form-check-label" for="hungerCheck">
						Hunger
					</label>
				</div>
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="elderlyCheck">
					<label class="form-check-label" for="elderlyCheck">
						Elderly
					</label>
				</div>
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="kidsCheck">
					<label class="form-check-label" for="kidsCheck">
						Kids
					</label>
				</div>
			</div>
		</div>
			
		<button class="accordion-button" @click="open">Advanced Options</button>
		<div class="accordion-panel">
			<div class="form-group">
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="closeToCTACheck">
					<label class="form-check-label" for="closeToCTACheck">
						Close to CTA
					</label>
				</div>
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="freeCheck">
					<label class="form-check-label" for="freeCheck">
						Free
					</label>
				</div>
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="noRSVPCheck">
					<label class="form-check-label" for="noRSVPCheck">
						No RSVP
					</label>
				</div>
				<div class="form-check">
					<input class="form-check-input" type="checkbox" value="" id="reoccurringCheck">
					<label class="form-check-label" for="reoccurringCheck">
						Reoccurring Events
					</label>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import Datepicker from 'vuejs-datepicker';
	export default{
		data() {
			return {
				state: {
					date: new Date(new Date().getFullYear(), new Date().getMonth() + 1,  new Date().getDate())
				}
			};
		},
		methods: {
			open: function(event) {
				event.target.classList.toggle('active');
				let panel = event.target.nextElementSibling;
				panel.classList.toggle('open');
				if (panel.style.maxHeight) {
					panel.style.maxHeight = null;
				}
				else {
					panel.style.maxHeight = panel.scrollHeight + 'px';
				} 
			}
		},
		components:{
			Datepicker
		}
	};
</script>