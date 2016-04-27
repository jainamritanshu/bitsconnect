from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Service(models.Model):
	user = models.ForeignKey(User, db_index=True)
	title = models.CharField(max_length=200,)
	content = models.CharField(max_length=500,)
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.title

class Classified(models.Model):
	user = models.ForeignKey(User, db_index=True)
	title = models.CharField(max_length=200,)
	content = models.CharField(max_length=500,)
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.title

class Bhavan(models.Model):
	name = models.CharField(max_length=10, db_index=True)

	def __str__(self):
		return self.name


class Event(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=200,)
	time = models.DateTimeField(db_index=True,)

	class Meta:
		permissions = (
            ("event_add", "Add events custom"),
            )

	def __str__(self):
		return self.title

class GlobalEvent(models.Model):
	title = models.CharField(max_length=200,)
	image = models.ImageField(upload_to= 'events/',)


	def __str__(self):
		return self.title

class Problem(models.Model):
	user = models.ForeignKey(User, db_index=True)
	title = models.CharField(max_length=200,)
	content = models.CharField(max_length=500,)
	bhavan = models.ForeignKey(Bhavan, db_index=True)
	votes = models.IntegerField(default=0, db_index=True)
	created = models.DateTimeField(auto_now_add=True,)

	class Meta:
		permissions = (
            ("problem_solve", "Solve problems SU"),
            )

	def __str__(self):
		return self.title

class Place(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return "(%s) %s"%(self.pk,self.name)

class Travel(models.Model):
	user = models.ForeignKey(User, db_index=True) 
	from_place = models.ForeignKey(Place, related_name="from_place", db_index=True)
	to_place = models.ForeignKey(Place, related_name="to_place", db_index=True)
	content = models.CharField(max_length=200,)
	date = models.DateTimeField(db_index=True)

	def __str__(self):
		return "%s --> %s"%(self.from_place.name, self.to_place.name)

class ProblemSolved(models.Model):
	user = models.ForeignKey(User,)
	title = models.CharField(max_length=200,)
	reply = models.CharField(max_length=500,)
	bhavan = models.ForeignKey(Bhavan, db_index=True)
	posted_on = models.DateTimeField()
	solved_by = models.ForeignKey(User,blank = True,null = True,related_name="solved_by")
	solved_on = models.DateTimeField(auto_now_add=True, db_index=True)

class MissedCall(models.Model):
	actor = models.ForeignKey(User,related_name='caller')
	user = models.ForeignKey(User,related_name='callee', db_index=True)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s --> %s"%(self.actor, self.user)


class ProblemVote(models.Model):
	problem = models.ForeignKey(Problem, related_name='voters')
	user = models.ForeignKey(User)

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.problem.votes+=1
			self.problem.save()
			super(ProblemVote, self).save(*args, **kwargs)
		else:
			return None

	def delete(self, *args, **kwargs):
		self.problem.votes-=1
		self.problem.save()
		super(ProblemVote, self).delete(*args, **kwargs)

	class Meta:
		unique_together = ('problem', 'user',)


@receiver(pre_delete, sender=GlobalEvent)
def event_delete(sender, instance, **kwargs):
	instance.image.delete(False)
	return 


class course(models.Model):
	name = models.CharField(max_length=9, default='')
	c_id = models.CharField(max_length=6, default=0)

	def __unicode__(self):
		return self.name


class notes(models.Model):
	notes = models.FileField(upload_to='notes/')
	course = models.ForeignKey(course)
	chapter = models.CharField(max_length=100)

	def __unicode__(self):
		return self.chapter


class handout(models.Model):
	handout = models.FileField(upload_to='handout/')
	course = models.ForeignKey(course)
	title = models.CharField(max_length=100)

	def __unicode__(self):
		return self.title

	
class books(models.Model):
	title = models.CharField(max_length=100)
	books = models.FileField(upload_to='books/')
	course = models.ForeignKey(course)

	def __unicode__(self):
		return self.title

class misc_no(models.Model):
	name = models.CharField(max_length=100)
	desig = models.CharField(max_length=100)
	num = models.IntegerField(default=0, db_index=True)		
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	def __unicode__(self):
		return self.name

class books_s(models.Model):
	course = models.ForeignKey(course)
	book = models.ForeignKey(books)
	is_delivered = models.BooleanField(default='False')
	is_approved = models.BooleanField(default='True')
	bhavan = models.ForeignKey(bhavan)
	room_no = models.IntegerField(default=0)	
	num_books = models.IntegerField(default=0)	
	comments = models.CharField(max_length=200, help_text="Guide the delivery boy")


