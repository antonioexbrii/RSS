<template>
  <v-layout justify-space-around class="ma-3 pa-2">
    <v-card centered class="ma-2 pa-2">
      <p class="display-3 text-xs-center">Formulário de Configuração</p>
      <p class="display-1 text-xs-center">Tabela de Urls</p>
      <v-layout>
        <v-flex xs11>
          <v-text-field
            class="mx-2"
            label="Url de RSS"
            v-model="url"
            required
            solo
          ></v-text-field>
        </v-flex>
        <v-flex xs1 class="text-xs-right">
          <v-btn
            right
            fab
            dark
            small
            color="blue darken-1"
            @click="adicionaUrl"
          >
            <v-icon dark>add</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>
      <v-data-table
        :headers="cabecalhosUrls"
        :items="urls"
        class="elevation-1 ma-2"
      >
        <template v-slot:items="props">
          <tr>
            <td>{{ props.item }}</td>
            <td class="text-xs-right">
              <v-btn
                fab
                dark
                small
                color="red darken-4"
                @click="removerURL(props.item)"
              >
                <v-icon dark>delete</v-icon>
              </v-btn>
            </td>
          </tr>
        </template>
        <template v-slot:no-data>
          <v-alert :value="true" color="warning" icon="warning"
            >Ainda não têm URLs...</v-alert
          >
        </template>
      </v-data-table>
      <p class="display-1 text-xs-center">Tabela de XPaths</p>
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
          <v-btn
            right
            fab
            dark
            small
            color="blue darken-1"
            @click="adicionaXPath"
          >
            <v-icon dark>add</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>
      <v-data-table
        :headers="cabecalhosXPaths"
        :items="xpaths"
        class="elevation-1 ma-2"
      >
        <template v-slot:items="props">
          <tr>
            <td>{{ props.item.campo }}</td>
            <td>{{ props.item.xpath }}</td>
            <td class="text-xs-right">
              <v-btn
                fab
                dark
                small
                color="red darken-4"
                @click="removerXPATH(props.item)"
              >
                <v-icon dark>delete</v-icon>
              </v-btn>
            </td>
          </tr>
        </template>
        <template v-slot:no-data>
          <v-alert :value="true" color="warning" icon="warning"
            >Ainda não têm XPATHs...</v-alert
          >
        </template>
      </v-data-table>
      <v-layout row wrap>
        <v-flex xs4>
          <v-text-field
            class="mx-2"
            label="Campo Chave"
            v-model="key"
            required
            solo
          ></v-text-field>
        </v-flex>
        <v-flex xs4>
          <v-text-field
            class="mx-2"
            label="Nome do Spider"
            v-model="spider_name"
            required
            solo
          ></v-text-field>
        </v-flex>
        <v-flex xs4>
          <v-text-field
            class="mx-2"
            label="Nome do Ficheiro de saida"
            v-model="file_name"
            required
            solo
          ></v-text-field>
        </v-flex>
      </v-layout>
      <v-flex xs4 offset-xs8>
        <v-btn dark large color="orange darken-2" @click="createFile"
          >Adicionar</v-btn
        >
      </v-flex>
    </v-card>
  </v-layout>
</template>

<script>
export default {
  data: () => ({
    cabecalhosUrls: [{ text: "Url" }, { text: "Ações" }],
    cabecalhosXPaths: [{ text: "Campo" }, { text: "XPATH" }, { text: "Ações" }],
    spider_name: "",
    file_name: "",
    url: "",
    urls: [],
    key: "",
    campo: "",
    xpath: "",
    xpaths: []
  }),
  methods: {
    adicionaUrl: function() {
      this.urls.push(this.url);
      this.url = "";
    },
    adicionaXPath: function() {
      this.xpaths.push({ campo: this.campo, xpath: this.xpath });
      this.campo = "";
      this.xpath = "";
    },
    removerURL: function(item) {
      var index = this.urls.indexOf(item);
      if (index > -1) {
        this.urls.splice(index, 1);
      }
    },
    removerXPATH: function(item) {
      for (var i in this.xpaths)
        if (this.xpaths[i] === item) {
          this.xpaths.splice(i, 1);
        }
    },
    createFile: function() {
      var index = -1;
      for (var z in this.xpaths)
        if (this.xpaths[z].campo === this.key) {
          index = z;
        }
      if (index === -1) alert("Campo Chave não encontrado");
      else {
        var str = `import scrapy
from scrapy.selector import XmlXPathSelector
import re
import json
from datetime import datetime

i=0

def filter(text):
  text = text.lower()
  text = re.sub(r'[\\'\\"]','',text)
  text = re.sub(r'[.!?:;,]','',text)
  return text
	
class ${this.spider_name.toUpperCase()}(scrapy.Spider):
  name = "${this.spider_name}"
  def start_requests(self):
    urls = [`;

        for (var i in this.urls)
          str += `
        '${this.urls[i]}',`;
        str += `
  ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    response.selector.remove_namespaces()
    global i
    filename='${this.file_name}'+str(i)+'.json'
    i += 1
    myDict=[]
`;
        for (var j in this.xpaths) {
          str += `
    ${this.xpaths[j].campo} = response.xpath('${
            this.xpaths[j].xpath
          }').extract()`;
        }
        str += `
    for item in zip(`;
        for (var b in this.xpaths) {
          if (b < this.xpaths.length) str += `${this.xpaths[b].campo},`;
          else str += `${this.xpaths[b].campo}`;
        }
        str += `):
      myDict.append({`;
        str += `
        'sentence': filter(item[${index}]),`;
        for (var k in this.xpaths) {
          str += `
        '${this.xpaths[k].campo}': item[${k}],`;
        }
        str += `
      })

    data = datetime.now()

    newDict = {
      "date": str(data),
      "entries": myDict
    }
    with open(filename, 'w', encoding='utf8') as f:
      json.dump(newDict,f, ensure_ascii=False)
      self.log('Fechou ficheiro %s' % filename)
      `;

        const blob = new Blob([str], { type: "text/plain" });
        const e = document.createEvent("MouseEvents"),
          a = document.createElement("a");
        a.download = this.spider_name + ".py";
        a.href = window.URL.createObjectURL(blob);
        a.dataset.downloadurl = ["text/json", a.download, a.href].join(":");
        e.initEvent(
          "click",
          true,
          false,
          window,
          0,
          0,
          0,
          0,
          0,
          false,
          false,
          false,
          false,
          0,
          null
        );
        a.dispatchEvent(e);
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
