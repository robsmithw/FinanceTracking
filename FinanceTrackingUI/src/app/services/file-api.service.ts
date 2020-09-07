import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../../environments/environment';

@Injectable()
export class FileApiService {

    constructor(private httpClient: HttpClient) {
    }

    public errorHandler(error: HttpErrorResponse){
        if (error.error instanceof HttpErrorResponse) {
        // A client-side or network error occurred.
            console.error('An error occurred:', error.error.message);
        } else {
            // The backend returned an unsuccessful response code.
            console.error(
                `Backend returned code ${error.status}, ` +
                `body was: ${error.error}`);
            console.log(error);
        }
        // Return an observable with a error message.
        return throwError('Error occured; please try again later.');
    }

    // GET template file
    getTemplate(): Observable<Blob> {
        return this.httpClient.get(`${API_URL}/downloadTemplate`, {responseType : 'blob'})
            .pipe(catchError(this.errorHandler));
    }
}
