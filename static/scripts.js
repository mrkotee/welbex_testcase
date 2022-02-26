
Vue.component(
    'v-table',
    {
  data: function () {
            return {
            sortKey: 'name',
            search_field: 'name',
            search_opt: 'equals',
            reverse: false,
            page: 1,
            per_page: 20,
            pages: 1,
            resources: [],
            }
  },
  created: function () {
        axios.post("/", {
                        page: 1,
                        per_page: this.per_page
                        }).then( res => (this.resources = res.data.resources, this.pages = res.data.pages)
                        );
  },
  methods: {
      	changePages() {
            this.page =  this.$refs.page.value;
            this.per_page = this.$refs.per_page.value;
        	axios.post("/table", {
        	    request: "change_page",
                page: this.page,
                per_page: this.per_page
        	}).then( res => (this.resources = res.data.resources, this.pages = res.data.pages) );
        },
        sortBy(sortKey) {
              this.reverse = (this.sortKey == sortKey) ? ! this.reverse : false;
              this.sortKey = sortKey;
        	axios.post("/table", {
        	    request: "sort",
                page: this.page,
                per_page: this.per_page,
                sort_field: sortKey,
                reverse: this.reverse,
        	}).then( res => (this.resources = res.data.resources, this.pages = res.data.pages) );
        },
        search() {
            axios.post("/table", {
                request: "search",
                page: this.page,
                per_page: this.per_page,
                search_field: this.search_field,
                search_opt: this.search_opt,
                search: this.$refs.search.value,
            }).then( res => (this.resources = res.data.resources, this.pages = res.data.pages) );
        },
  },

  template: `
    <div>
    <select name="search_field"  ref="search_field" v-model="search_field">
            <option selected value="date">Дата</option>
            <option value="name">Название</option>
            <option value="amount">Количество</option>
            <option value="distance">Расстояние</option>
    </select>
    <select name="search_opt" @change="search()"  ref="search_opt" v-model="search_opt">
            <option selected value="equals">равно</option>
            <option v-if="search_field != 'date' && search_field != 'amount' && search_field != 'distance'" value="into">содержит</option>
            <option v-if="search_field != 'name'" value="larger">больше</option>
            <option v-if="search_field != 'name'" value="less">меньше</option>
    </select>
    <input v-if="search_field === 'date'" type='date' @change="search()" ref="search" placeholder="Поиск ">
    <input v-else @change="search()" ref="search" placeholder="Поиск ">
    кол-во на странице<select name="per_page" @change="changePages()"  ref="per_page" v-model="per_page">
        <option selected value=20>20</option><option value=40>40</option>
    </select>
    страница<select name="page" @change="changePages()"  ref="page" v-model="page" >
           <option v-for="inx in parseInt(pages)" :key="inx" >{{ inx }}</option>
    </select>
    <table border="1">
         <tr>
             <th>Дата</th>
             <th><a href="#" @click="sortBy('name')">Название</a></th>
             <th><a href="#" @click="sortBy('amount')">Количество</a></th>
             <th><a href="#" @click="sortBy('distance')">Расстояние</a></th>
         </tr>
        <tr v-for="res in resources">
            <td>{{ res.date }}</td>
            <td>{{ res.name }}</td>
            <td>{{ res.amount }}</td>
            <td>{{ res.distance }}</td>
        </tr>
        </table>
    </div>`
})

let app = new Vue({ el: '#app', data: {
    },

    computed: {

    },
    methods: {

    },
    })