import { Component, OnInit, OnDestroy} from '@angular/core';
import { TestApiService } from './services/test-api.service';
import { Subscription } from 'rxjs';
import { Test } from './models/test.model';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'FinanceTrackingUI';
  testListSub: Subscription;
  testList: Test[];

  constructor(private testApi: TestApiService, private toastr: ToastrService){

  }

  ngOnInit(){
    this.testListSub = this.testApi.getTest()
      .subscribe(res => {
        this.testList = res;
        this.toastr.success('Successfully retrieved data');
      },
      err => {
        this.toastr.error(err);
      }
      );
  }
  ngOnDestroy(){
    this.testListSub.unsubscribe();
  }

}
