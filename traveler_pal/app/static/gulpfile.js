// 引入 gulp
var gulp = require('gulp');

// 引入组件
var jshint = require('gulp-jshint');
var sass = require('gulp-sass');
var minifycss = require('gulp-minify-css');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var del = require('del');

// 检查脚本
gulp.task('lint', function() {
    return gulp.src('./tep/js/*.js')
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

// 编译Sass
gulp.task('sass', function() {
    return gulp.src('./tep/scss/app.scss')
        .pipe(sass())
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('./css'));
});

// 合并，压缩文件
gulp.task('scripts', function() {
    return gulp.src('./tep/js/*.js')
        .pipe(concat('all.js'))
        .pipe(rename('all.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('./js'));
});

gulp.task('clean', function(callback) {
    del(['./css/app.min.css', './js/all.min.js'], callback)
});

// 默认任务
gulp.task('default', function(){
    gulp.run('lint', 'sass', 'scripts', 'clean');

    // 监听文件变化
    gulp.watch('./tep/js/*.js', function(){
        gulp.run('lint', 'sass', 'scripts', 'clean');
    });

    gulp.watch('./tep/scss/*.scss', function(){
        gulp.run('lint', 'sass', 'scripts', 'clean');
    });
});
