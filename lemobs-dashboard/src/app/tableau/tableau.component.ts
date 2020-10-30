import { Component, ViewChild, ElementRef, AfterViewInit } from "@angular/core";

declare var tableau: any;

@Component({
  selector: 'app-tableau',
  templateUrl: './tableau.component.html',
  styleUrls: ['./tableau.component.css']
})
export class TableauComponent implements AfterViewInit {
  viz: any;
  @ViewChild("vizContainer") containerDiv: ElementRef;

  ngAfterViewInit() {
    this.initTableau();
  }

  initTableau() {
  }
}
