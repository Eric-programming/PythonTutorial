import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { NodeComponent } from './node/node.component';
import { RemoveHostDirective } from './remove-host.directive';

@NgModule({
  declarations: [
    AppComponent,
    NodeComponent,
    RemoveHostDirective
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
