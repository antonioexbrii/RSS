<template>
  <v-layout justify-space-around  class="ma-3">
    <v-card centered>
      <p class="display-3 text-xs-center">Formulário de Configuração</p>
      <v-form ref="form" v-model="valid" lazy-validation>
      <v-layout row wrap>
      <v-flex xs6> 
        <v-text-field
          class='mx-2'
          label="Nome do Spider"
          v-model="spider_name"
          required
          solo
        ></v-text-field>
      </v-flex> 
      <v-flex xs6>
        <v-text-field
          class='mx-2'
          label="Nome do Ficheiro de saida"
          v-model="file_name"
          required
          solo
        ></v-text-field>
      </v-flex>
    </v-layout>
    </v-form>
      <p class="display-3 text-xs-center">Tabela de Urls</p>
      <v-layout>
        <v-flex xs11>
          <v-text-field
            class='mx-2'
            label="Url de RSS"
            v-model="url"
            required
            solo
          ></v-text-field>  
        </v-flex>
        <v-flex xs1 class="text-xs-right">
            <v-btn right fab dark small color="blue darken-1" @click="adicionaUrl">
              <v-icon dark>add</v-icon>
            </v-btn>
        </v-flex>
      </v-layout>
      <v-data-table
            :headers="cabecalhosUrls"
            :items="urls"
            class="elevation-1"
        >
            <template v-slot:items="props">
              <tr>
                <td >{{ props.item }}</td>
                <td class="text-xs-right" >
                  <v-btn fab dark small color="red darken-4" @click="removerURL(props.item)">
                    <v-icon dark>delete</v-icon>
                  </v-btn>
                </td>
              </tr>
            </template>
            <template v-slot:no-data>
              <v-alert :value="true" color="warning" icon="warning">
                Ainda não têm URLs...
              </v-alert>
            </template>
        </v-data-table>
      <p class="display-3 text-xs-center">Tabela de XPaths</p>
      <v-layout>
        <v-flex xs5>
          <v-text-field
            class="mx-2"
            label="Nome do Campo"
            v-model="campo"
            required
            solo
          ></v-text-field>
        </v-flex>
        <v-flex xs6>
            <v-text-field
                class="mx-2"
                label="XPath"
                v-model="xpath"
                required
                solo
            ></v-text-field>
        </v-flex>
        <v-flex xs1 class="text-xs-right">
            <v-btn right fab dark small color="blue darken-1" @click="adicionaXPath">
              <v-icon dark>add</v-icon>
            </v-btn>
        </v-flex>
      </v-layout>
      <v-data-table
            :headers="cabecalhosXPaths"
            :items="xpaths"
            class="elevation-1"
        >
            <template v-slot:items="props">
              <tr>
                <td >{{ props.item.campo }}</td>
                <td >{{ props.item.xpath }}</td>
                <td class="text-xs-right" >
                  <v-btn fab dark small color="red darken-4" @click="removerXPATH(props.item)">
                    <v-icon dark>delete</v-icon>
                  </v-btn>
                </td>
              </tr>
            </template>
            <template v-slot:no-data>
              <v-alert :value="true" color="warning" icon="warning">
                Ainda não têm XPATHs...
              </v-alert>
            </template>
        </v-data-table>
    </v-card>
  </v-layout>
</template>

<script>
export default {
  data: () => ({
      cabecalhosUrls: [{text: 'Url'},{text: 'Ações'}],
      cabecalhosXPaths: [{text: 'Campo'},{text: 'XPATH'},{text: 'Ações'}],
      spider_name: '',
      file_name: '',
      url: '',
      urls: [],
      campo: '',
      xpath: '',
      xpaths: []
  }),
  methods: {
    adicionaUrl: function() {
      this.urls.push(this.url)
      this.url = ''
    },
    adicionaXPath: function() {
      this.xpaths.push({campo: this.campo,xpath: this.xpath})
      this.campo = ''
      this.xpath = ''
    },
    removerURL: function(item) {
      var index = this.urls.indexOf(item);
      if (index > -1) {
        this.urls.splice(index, 1);
      }
    },
    removerXPATH: function(item) {
      for(var i in this.xpaths)
        if (this.xpaths[i]===item) {
          this.xpaths.splice(i, 1);
        }
    }
  }
};
</script>

<style lang="scss" scoped></style>
