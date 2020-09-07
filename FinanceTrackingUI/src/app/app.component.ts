import { Component, OnInit, OnDestroy} from '@angular/core';
import { TestApiService } from './services/test-api.service';
import { Subscription } from 'rxjs';
import { saveAs } from 'file-saver';
import { Test } from './models/test.model';
import { ToastrService } from 'ngx-toastr';
import { FileApiService } from './services/file-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'FinanceTracking';
  testListSub: Subscription;
  downloadTempSub: Subscription;
  testList: Test[];

  constructor(private testApi: TestApiService, private downloadApi: FileApiService, private toastr: ToastrService){

  }

  ngOnInit(){
    this.testListSub = this.testApi.getTest()
      .subscribe(res => {
        this.testList = res;
        this.toastr.success('Successfully retrieved test data');
      },
      err => {
        this.toastr.error(err);
      });
  }

  downloadTemplate(){
    this.downloadTempSub = this.downloadApi.getTemplate()
      .subscribe(
        res => {
          saveAs(res, 'template.csv');
          this.toastr.success('Successfully downloaded template');
        },
        err => {
          this.toastr.error(err);
        });
  }

  ngOnDestroy(){
    this.testListSub.unsubscribe();
    this.downloadTempSub.unsubscribe();
  }

}
