# Create visualizations for event distribution and user behavior
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# 1. Event Distribution Pie Chart
event_counts = events_df['event'].value_counts()
ax1.pie(event_counts, labels=event_counts.index, autopct='%1.1f%%', colors=sns.color_palette('Set3'))
ax1.set_title('Distribution of Event Types')

# 2. Daily Events Timeline
daily_events = events_df.groupby([events_df['timestamp'].dt.date, 'event']).size().unstack()
daily_events.plot(ax=ax2)
ax2.set_title('Daily Events Over Time')
ax2.set_xlabel('Date')
ax2.set_ylabel('Number of Events')
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)

# 3. Conversion Funnel
funnel_data = event_counts.iloc[::-1]  # Reverse order for funnel
ax3.bar(range(len(funnel_data)), funnel_data, color=sns.color_palette('Set3'))
ax3.set_title('Conversion Funnel')
ax3.set_xticks(range(len(funnel_data)))
ax3.set_xticklabels(funnel_data.index)
ax3.set_ylabel('Number of Events')

# 4. Hourly Pattern
events_df['hour'] = events_df['timestamp'].dt.hour
hourly_events = events_df.groupby(['hour', 'event']).size().unstack()
hourly_events.plot(ax=ax4)
ax4.set_title('Hourly Event Patterns')
ax4.set_xlabel('Hour of Day')
ax4.set_ylabel('Number of Events')

plt.tight_layout()
plt.show()

# Calculate key metrics
print("\nKey Metrics:")
print("-" * 50)

# 1. Conversion Rates
cart_to_view_rate = (event_counts['addtocart'] / event_counts['view']) * 100
purchase_to_cart_rate = (event_counts['transaction'] / event_counts['addtocart']) * 100
purchase_to_view_rate = (event_counts['transaction'] / event_counts['view']) * 100

print(f"Cart to View Rate: {cart_to_view_rate:.2f}%")
print(f"Purchase to Cart Rate: {purchase_to_cart_rate:.2f}%")
print(f"Purchase to View Rate: {purchase_to_view_rate:.2f}%")

# 2. User Activity Metrics
unique_users = events_df['visitorid'].nunique()
unique_items = events_df['itemid'].nunique()
avg_events_per_user = len(events_df) / unique_users

print(f"\nUnique Users: {unique_users:,}")
print(f"Unique Items: {unique_items:,}")
print(f"Average Events per User: {avg_events_per_user:.2f}")

# 3. Daily Activity
events_per_day = daily_events.sum(axis=1)
print(f"\nAverage Daily Events: {events_per_day.mean():.0f}")
print(f"Busiest Day: {events_per_day.idxmax()} with {events_per_day.max():.0f} events")
print(f"Slowest Day: {events_per_day.idxmin()} with {events_per_day.min():.0f} events") 