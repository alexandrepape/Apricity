<template>
  <div>
    <br>
    <div.title>
        Select demographic data
    </div.title>
    <br>
    <br>
    <select @click="getDemo" v-model="selected">
      <option disabled value="True">Selected</option>
      <option>class of worker</option>
      <option>industry code</option>
      <option>occupation code</option>
      <option>education</option>
      <option>wage per hour</option>
      <option>last education</option>
      <option>marital status</option>
      <option>major industry code</option>
      <option>major occupation code</option>
      <option>mace</option>
      <option>hispanice</option>
      <option>sex</option>
      <option>member of labor</option>
      <option>reason for unemployment</option>
      <option>fulltime</option>
      <option>capital gain</option>
      <option>capital loss</option>
      <option>dividends</option>
      <option>income tax liability</option>
      <option>previus residence region</option>
      <option>previus residence state</option>
      <option>household-with-family</option>
      <option>household-simple</option>
      <option>weight</option>
      <option>msa-change</option>
      <option>reg-change</option>
      <option>within-reg-change</option>
      <option>lived-here</option>
      <option>migration prev res in sunbelt</option>
      <option>num persons worked for employer</option>
      <option>family members under 118</option>
      <option>father birth country</option>
      <option>mother birth country</option>
      <option>birth country</option>
      <option>citizenship</option>
      <option>own business or self employed</option>
      <option>veterans benefits</option>
      <option>weeks worked in year</option>
      <option>year</option>
      <option>salary range</option>
    </select>
    <br>
    <br>
    <br>
    <br>
    <table align="center">
    <thead>
        <tr>
            <th colspan="1">Value</th>
            <th colspan="1">average age </th>
            <th colspan="1">count </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>{{value}}</td>
            <td>{{avg}}</td>
            <td>{{count}}</td>
        </tr>
    </tbody>
</table>
  </div>
</template>
<script>
import {HTTP} from '../http-constant'
export default {
  name: 'ShowDemographic',
  data () {
    return {
      value: '',
      count: '',
      avg: ''
    }
  },
  methods: {
    getDemo: function () {
      HTTP.get('/all/' + this.selected)
        .then(response => {
          var arrValue = []
          var arrCount = []
          var arrAvg = []
          var objectLength = Object.keys(response.data).length
          for (var i = 1; i <= objectLength; i++) {
            arrValue.push(response.data[i].value)
            arrCount.push(response.data[i].count)
            arrAvg.push(response.data[i].avg_age)
          }
          /* eslint-disable */
          this.value = arrValue.join("\n")
          this.count = arrCount.join("\n")
          this.avg = arrAvg.join("\n")
        })
        .catch(e => {
          this.errors = e
        })
    }
  }
}
</script>

<style scoped>
div.title {
  font-size: 150px;
}

body {
  font-family: Helvetica Neue, Arial, sans-serif;
  font-size: 14px;
  color: #444;
}

table {
  border: 2px solid #42b983;
  border-radius: 3px;
  background-color: #fff;
}

th {
  background-color: #42b983;
  color: #fff;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

td {
  white-space:pre;
  background-color: #f9f9f9;
}

th, td {
  white-space:pre;
  min-width: 120px;
  padding: 10px 20px;
}

th.active {
  color: #fff;
}

th.active .arrow {
  opacity: 1;
}

.arrow {
  display: inline-block;
  vertical-align: middle;
  width: 0;
  height: 0;
  margin-left: 5px;
  opacity: 0.66;
}

.arrow.asc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-bottom: 4px solid #fff;
}

.arrow.dsc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 4px solid #fff;
}
</style>
